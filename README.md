
# Contact Directory REST API
### REST API Debugging & Enhancement Challenge — Task 2

**Organization:** Vision Orbit Innovations  
**Developer:** Elakiya S.  
**Technology:** Python, FastAPI, Pydantic, Pytest

---

## 1. Project Overview

The Contact Directory REST API is a Python-based backend application developed using FastAPI.

This project was completed as part of the Vision Orbit Innovations REST API Debugging & Enhancement Challenge.

The objective was to identify existing bugs, fix incorrect API behavior, implement proper input validation, improve exception handling, and write automated tests.

The application supports creating, retrieving, searching, updating, and deleting contact records.

## 2. Technologies Used

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- Git and GitHub

## 3. Features

- Create new contacts
- Retrieve all contacts
- Retrieve a contact using its ID
- Filter contacts by email
- Update existing contact information
- Delete contacts
- Prevent duplicate email addresses
- Validate names, emails, and phone numbers
- Return meaningful HTTP error responses
- Automated API testing

## 4. API Endpoints

| Method | Endpoint | Description | Success Code |
|--------|----------|-------------|--------------|
| GET | `/` | API health check | 200 |
| GET | `/contacts` | Retrieve all contacts | 200 |
| GET | `/contacts?email=...` | Filter contacts by email | 200 |
| GET | `/contacts/{contact_id}` | Retrieve contact by ID | 200 |
| POST | `/contacts` | Create a new contact | 201 |
| PATCH | `/contacts/{contact_id}` | Update a contact | 200 |
| DELETE | `/contacts/{contact_id}` | Delete a contact | 200 |

## 5. Bugs Identified and Fixed

### Bug 1: Incorrect Email Filtering

**Problem:** The email filtering logic returned contacts that did not match the requested email.

**Fix:** Corrected the comparison condition to return matching contacts.

**Result:** Email filtering now returns the expected contact records.

### Bug 2: Duplicate Email Handling

**Problem:** The API allowed multiple contacts to use the same email address.

**Fix:**
- Added duplicate email validation during contact creation.
- Added duplicate email validation during contact updates.
- Used case-insensitive email comparison.

**Result:** Duplicate email requests return HTTP `409 Conflict`.

### Bug 3: Missing Input Validation

**Problem:** Invalid contact details could be submitted.

**Fix:** Implemented Pydantic validation.

Validation rules:

| Field | Validation |
|-------|------------|
| Name | Minimum 2 and maximum 50 characters |
| Email | Valid email address format |
| Phone | Exactly 10 numeric digits |

**Result:** Invalid requests return HTTP `422 Unprocessable Entity`.

### Bug 4: Contact Update Validation

**Problem:** Contact updates required better validation and error handling.

**Fix:**
- Added validation for PATCH requests.
- Prevented duplicate email updates.
- Rejected explicit null values for contact fields.
- Added checks for nonexistent contact IDs.

**Result:** Contact updates return appropriate success or error responses.

### Bug 5: Incorrect Delete Behavior

**Problem:** The API returned a success message even when the requested contact did not exist.

**Fix:** Added a contact existence check before deletion.

**Result:** Deleting a nonexistent contact returns HTTP `404 Not Found`.

## 6. HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Successful request |
| 201 | Contact created successfully |
| 404 | Contact not found |
| 409 | Duplicate email conflict |
| 422 | Invalid request data |

## 7. Installation and Setup

### Prerequisites

- Python 3.10 or newer
- pip
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/elakiyasakthivel27/Contact-Directory-REST-API.git
cd Contact-Directory-REST-API
```

### Step 2: Create a Virtual Environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Start the FastAPI Server

```bash
python -m uvicorn main:app --reload
```

### Step 5: Open API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

The Swagger interface can be used to execute and test all available API endpoints.

## 8. Example API Requests

### Create Contact

**POST** `/contacts`

Request body:

```json
{
  "name": "Kavya",
  "email": "kavya@example.com",
  "phone": "9876543210"
}
```

Expected response status: `201 Created`

### Update Contact

**PATCH** `/contacts/1`

Request body:

```json
{
  "phone": "9123456780"
}
```

Expected response status: `200 OK`

### Filter Contacts

**GET** `/contacts?email=nila@example.com`

Expected response status: `200 OK`

### Delete Contact

**DELETE** `/contacts/2`

Expected response status: `200 OK`

## 9. Automated Testing

Automated testing was implemented using Pytest and FastAPI TestClient.

The tests verify successful API operations, input validation, duplicate email handling, and error responses.

### Test Cases

| No. | Test Case | Result |
|-----|-----------|--------|
| 1 | API health check | Passed |
| 2 | Retrieve all contacts | Passed |
| 3 | Create new contact | Passed |
| 4 | Reject duplicate email during creation | Passed |
| 5 | Reject invalid contact data | Passed |
| 6 | Update existing contact | Passed |
| 7 | Delete existing contact | Passed |
| 8 | Delete nonexistent contact | Passed |
| 9 | Retrieve nonexistent contact | Passed |
| 10 | Reject duplicate email during update | Passed |
| 11 | Reject invalid phone during update | Passed |
| 12 | Reject null name during update | Passed |
| 13 | Update nonexistent contact | Passed |
| 14 | Filter contacts by email | Passed |

### Run Automated Tests

```bash
python -m pytest test_main.py -v
```

### Test Execution Result

```text
================ Test Summary ================

14 tests collected
14 tests passed
0 tests failed
1 dependency deprecation warning

Execution time: 0.73 seconds

==============================================
```

**Result: All 14 automated tests passed successfully.**

The warning originated from the Starlette TestClient dependency and did not affect test execution.

## 10. Project Structure

```text
Contact-Directory-REST-API/
|
|-- main.py
|-- test_main.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

### File Descriptions

- `main.py` — FastAPI application, contact endpoints, validation, and error handling.
- `test_main.py` — Automated tests for API functionality.
- `requirements.txt` — Python project dependencies.
- `README.md` — Project documentation.
- `.gitignore` — Excludes temporary and environment-specific files.

## 11. Assumptions and Limitations

- Contact data is stored in an in-memory Python dictionary.
- Data is not persisted when the application restarts.
- Each contact is assigned a unique ID.
- Email addresses must be unique.
- Phone numbers must contain exactly 10 digits.
- No database or authentication system is included.
- No frontend is required for this assessment.

## 12. Conclusion

The Contact Directory REST API was successfully debugged and enhanced by correcting email filtering, preventing duplicate emails, implementing Pydantic validation, improving PATCH and DELETE operations, and handling API errors using appropriate HTTP status codes.

A total of 14 automated test cases were executed successfully using Pytest.

The completed project demonstrates REST API development, debugging, validation, exception handling, automated testing, and Git-based version control.

---

**Submitted by:** Elakiya S.  
**Assessment:** Task 2 — REST API Debugging & Enhancement Challenge  
**Organization:** Vision Orbit Innovations

**GitHub Repository:**  
https://github.com/elakiyasakthivel27/Contact-Directory-REST-API
