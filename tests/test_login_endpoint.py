import pytest
import requests
import uuid


BASE_URL = "http://restapi.adequateshop.com/api/AuthAccount"
EMAIL = f"{str(uuid.uuid4())}@aaa.com"
PASSWD = "secret"


def test_registration():
    """
    Creating test user
    """
    data = {
        "name": "AAA",
        "email": EMAIL,
        "password": PASSWD
    }
    url = f"{BASE_URL}/Registration"
    response = requests.post(url, json=data)
    assert response.status_code == 200, "ATTENTION: User was not created"


@pytest.mark.parametrize("data", [
    {
        "email": EMAIL,
        "password": PASSWD,
        "expected_status": 200,
        "expected_message": "success",
        "expected_errors": None
    },
    {
        "email": "wrong@email.com",
        "password": PASSWD,
        "expected_status": 200,
        "expected_message": "invalid username or password",
        "expected_errors": None
    },
    {
        "email": EMAIL,
        "password": "wrongpassword",
        "expected_status": 200,
        "expected_message": "invalid username or password",
        "expected_errors": None
    },
    {
        "email": "",
        "password": PASSWD,
        "expected_status": 400,
        "expected_message": "the request is invalid.",
        "expected_errors": {
            "log.email": ["field is required"]
        }
    },
    {
        "email": EMAIL,
        "password": "",
        "expected_status": 400,
        "expected_message": "the request is invalid.",
        "expected_errors": {
            "log.password": ["field is required"]
        }
    },
    {
        "email": EMAIL,
        "password": None,
        "expected_status": 400,
        "expected_message": "the request is invalid.",
        "expected_errors": {
            "log.password": ["field is required"]
        }
    },
    {
        "email": None,
        "password": PASSWD,
        "expected_status": 400,
        "expected_message": "the request is invalid.",
        "expected_errors": {
            "log.email": ["field is required"]
        }
    }
])
def test_login(data):
    """
    Test the login endpoint with different data parameters.
    """
    url = f"{BASE_URL}/Login"
    response = requests.post(url, json=data)
    assert response.status_code == data["expected_status"], f"Expected code: {data['expected_status']}, Actual code: {response.status_code}"

    # Based on the status code, response structure will be different. This retrieves the message regardless of case
    response_json = response.json()
    message = response_json.get("message", response_json.get("Message", "")).lower()
    expected_message = data["expected_message"].lower()
    assert message == expected_message, f"Expected message: {expected_message}, Actual message: {message}"

    # If there is error description hidden inside "ModelState"
    if data["expected_errors"] is not None:
        errors = response_json.get("ModelState", {})
        expected_errors = data["expected_errors"]
        assert errors == expected_errors
