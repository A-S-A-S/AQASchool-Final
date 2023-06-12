import pytest
import requests
import logging
import uuid

BASE_URL = "http://restapi.adequateshop.com/api"

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


@pytest.fixture
def new_tourist():
    # Generate a unique ID for the tourist
    tourist_id = str(uuid.uuid4())

    # Create a new tourist
    tourist_data = {
        "id": 0,
        "tourist_name": "AAA",
        "tourist_email": f"{tourist_id}@aaa.com",
        "tourist_location": "AAA",
        "createdat": "2023-06-10T18:24:44.755Z"
    }

    response = requests.post(f"{BASE_URL}/Tourist", json=tourist_data)
    assert response.status_code == 201
    print(
        f"POST '/Tourist' endpoint responded with "
        f"{response.status_code} status code and "
        f"{response.text}"
    )
    return response.json()["id"]


def test_delete_tourist_success(new_tourist):
    # Delete the tourist
    response = requests.delete(f"{BASE_URL}/Tourist/{new_tourist}")
    print(
        f"DELETE '/Tourist' endpoint responded with "
        f"{response.status_code} status code and "
        f"{response.text}"
    )
    assert response.status_code == 200


"""

def test_delete_tourist_twice(new_tourist):
    # Try to delete the same tourist twice
    response1 = requests.delete(f"{BASE_URL}/Tourist/{new_tourist}")
    assert response1.status_code == 204

    response2 = requests.delete(f"{BASE_URL}/Tourist/{new_tourist}")
    assert response2.status_code == 404
"""
