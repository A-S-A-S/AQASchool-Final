import requests
import pytest
from datetime import datetime


BASE_URL = "http://restapi.adequateshop.com/api"


@pytest.fixture(scope="module")
def created_tourist():
    """
    Creating test user
    """
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    email = f"john_{ts}@example.com"
    data = {
        "id": 0,
        "tourist_name": "John Doe",
        "tourist_email": email,
        "tourist_location": "New York",
        "createdat": ts
    }
    url = f"{BASE_URL}/Tourist"
    response = requests.post(url, json=data)
    created_tourist = response.json()

    yield created_tourist


def test_get_tourist_success(created_tourist):
    """
    Happy path
    """
    tourist_id = created_tourist["id"]
    url = f"{BASE_URL}/Tourist/{tourist_id}"
    response = requests.get(url)
    tourist_data = response.json()
    # POST /Tourist added "Z" suffix
    # But it is not present in the GET response, so:
    created_tourist["createdat"] = created_tourist["createdat"].rstrip("Z")
    assert tourist_data == created_tourist


def test_get_tourist_not_found():
    """
    Verify 404 error
    If you want to verify that the id is not present for sure
    Call GET {{url}}/api/Tourist. But this will degrade performance
    """
    url = f"{BASE_URL}/Tourist/9999"
    response = requests.get(url)

    assert response.status_code == 404
    assert response.content == b""  # Empty response body


@pytest.mark.parametrize("param", ["abc", None])
def test_get_tourist_invalid_id(param):
    """
    Cases for invalid payload
    """
    url = f"{BASE_URL}/Tourist/{param}"
    response = requests.get(url)
    error_data = response.json()

    assert response.status_code == 400
    assert error_data["Message"] == "The request is invalid."


@pytest.mark.parametrize("param", [
    "%3Ffilter%3Did%20eq%209999",
    "%3Furl%3Dhttp%3A%2F%2Fwww.google.com%2F"
])
def test_get_tourist_server_error(param):
    """
    Verify 400 error
    First of all, it should not be this way, so I won't check the body
    """
    url = f"{BASE_URL}/Tourist/{param}"
    response = requests.get(url)

    assert response.status_code == 400
