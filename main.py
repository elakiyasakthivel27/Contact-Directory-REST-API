from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(title="Contact Directory API")

contacts = {
    1: {"id": 1, "name": "Nila", "email": "nila@example.com", "phone": "9000000001"},
    2: {"id": 2, "name": "Arun", "email": "arun@example.com", "phone": "9000000002"},
}
next_id = 3


class ContactCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(pattern=r"^[0-9]{10}$")


class ContactUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, pattern=r"^[0-9]{10}$")


@app.get("/")
def health():
    return {"message": "Contact Directory API is running"}


@app.get("/contacts")
def list_contacts(email: str | None = None):
    results = list(contacts.values())
    if email:
        # TODO: Review filtering behavior.
        results = [c for c in results if c["email"] == email]
    return results


@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    if contact_id not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contacts[contact_id]


@app.post("/contacts", status_code=201)
def create_contact(payload: ContactCreate):
    global next_id

    # Check for duplicate email
    for existing_contact in contacts.values():
        if existing_contact["email"].lower() == payload.email.lower():
            raise HTTPException(
                status_code=409,
                detail="A contact with this email already exists"
            )

    contact = {
        "id": next_id,
        "name": payload.name,
        "email": payload.email,
        "phone": payload.phone,
    }

    contacts[next_id] = contact
    next_id += 1
    return contact


@app.patch("/contacts/{contact_id}")
def update_contact(contact_id: int, payload: ContactUpdate):
    if contact_id not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    updates = payload.model_dump(exclude_unset=True)
    if any(value is None for value in updates.values()):
        raise HTTPException(
            status_code=422,
            detail="Contact fields cannot be null"
        )
    if "email" in updates and updates["email"] is not None:
       for existing_id, existing_contact in contacts.items():
            if existing_id != contact_id:
                if existing_contact["email"].lower() == updates["email"].lower():
                    raise HTTPException(
                        status_code=409,
                        detail="A contact with this email already exists"
                    )
    contacts[contact_id].update(updates)
    return contacts[contact_id]


@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    if contact_id not in contacts:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )

    contacts.pop(contact_id)
    return {"message": "Contact deleted successfully"}
