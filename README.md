# Task 2 — Contact Directory REST API Debugging Challenge

## Scenario
The API stores contact records and contains bugs around filtering, updates, duplicate email handling, and deletion.

The project below is intentionally incomplete and contains defects. Review the existing code, fix it, and demonstrate your changes with automated tests.

## Requirements
1. Identify and fix the existing bugs.
2. Add suitable input validation.
3. Return meaningful errors and correct HTTP status codes.
4. Write automated tests for normal requests and failure cases.
5. Update this README with setup steps, bugs found, changes made, and test results.

## Setup
Use Python 3.10 or newer.

### Windows Command Prompt
```bat
py -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the API.

## Submission
- GitHub repository link
- Updated source code
- Automated tests and test output
- Updated README with your findings and assumptions

## Rules
- A frontend is not required.
- You may use documentation and AI coding tools, but you must explain your changes during a short review.
- Do not add real passwords, API keys, or confidential information.

**Suggested deadline:** Within 48 hours of receiving the task.
