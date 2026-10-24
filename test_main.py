import copy
import pytest
import main
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
@pytest.fixture(autouse=True)
def reset_contacts():
    original_contacts = copy.deepcopy(main.contacts)
    original_next_id = main.next_id

    yield

    main.contacts.clear()
    main.contacts.update(original_contacts)
    main.next_id = original_next_id


def test_health():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Contact Directory API is running"
    }
#Get All Contacts
def test_get_contacts():
    response = client.get("/contacts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1

#Create a Contact
def test_create_contact():
    new_contact = {
        "name": "Kavya",
        "email": "kavya@example.com",
        "phone": "9876543210"
    }

    response = client.post("/contacts", json=new_contact)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Kavya"
    assert data["email"] == "kavya@example.com"
    assert data["phone"] == "9876543210"
    assert "id" in data

#Duplicate Email Rejection
def test_duplicate_email():
    duplicate_contact = {
        "name": "Another Nila",
        "email": "nila@example.com",
        "phone": "9876543210"
    }

    response = client.post(
        "/contacts",
        json=duplicate_contact
    )

    assert response.status_code == 409

    assert response.json()["detail"] == (
        "A contact with this email already exists"
    )

#Invalid Input Validation
def test_invalid_contact():
    invalid_contact = {
        "name": "A",
        "email": "invalidemail",
        "phone": "12345"
    }

    response = client.post(
        "/contacts",
        json=invalid_contact
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert len(errors) >= 3

#Update Contact (PATCH)
def test_update_contact():
    updated_data = {
        "phone": "9123456780"
    }

    response = client.patch(
        "/contacts/1",
        json=updated_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["phone"] == "9123456780"

#Delete Contact
def test_delete_contact():
    response = client.delete("/contacts/2")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Contact deleted successfully"
    }

    # Confirm the contact no longer exists
    check_response = client.get("/contacts/2")

    assert check_response.status_code == 404

#Delete a Nonexistent Contact
def test_delete_nonexistent_contact():
    response = client.delete("/contacts/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contact not found"
    }

#Test GET Contact Not Found (404)
def test_get_nonexistent_contact():
    response = client.get("/contacts/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contact not found"
    }

#Test PATCH Duplicate Email (409)
def test_update_duplicate_email():
    updated_data = {
        "email": "nila@example.com"
    }

    response = client.patch(
        "/contacts/2",
        json=updated_data
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": "A contact with this email already exists"
    }

#Test Invalid PATCH Input (422)
def test_update_invalid_phone():
    updated_data = {
        "phone": "12345"
    }

    response = client.patch(
        "/contacts/1",
        json=updated_data
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert len(errors) >= 1
    assert errors[0]["loc"][-1] == "phone"

#Test PATCH with Null Value (422)
def test_update_null_name():
    updated_data = {
        "name": None
    }

    response = client.patch(
        "/contacts/1",
        json=updated_data
    )

    assert response.status_code == 422

    assert response.json() == {
        "detail": "Contact fields cannot be null"
    }

#Test PATCH Contact Not Found (404)
def test_update_nonexistent_contact():
    updated_data = {
        "name": "Kavya"
    }

    response = client.patch(
        "/contacts/999",
        json=updated_data
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contact not found"
    }

#Test Email Filtering (GET)
def test_filter_contacts_by_email():
    response = client.get(
        "/contacts",
        params={"email": "nila@example.com"}
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Nila"
    assert data[0]["email"] == "nila@example.com"