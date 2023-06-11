import unittest
import requests
import logging
import datetime

class AuthAccountLoginTestSuit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configure logging
        cls.log = logging.getLogger(__name__)
        cls.log.setLevel(logging.DEBUG)
        cls.log.addHandler(logging.StreamHandler())

        # Set up the basics
        cls.base_url = "http://restapi.adequateshop.com/api/AuthAccount"
        cls.headers = {"Content-Type": "application/json"}
        # Unique email based on current timestamp
        cls.date = datetime.datetime.now()
        cls.email = cls.date.strftime("%H%M%S") + "@haiyaa.com"
        cls.password = cls.date.timestamp()

        # Create user
        user_payload = {
            "name": "AAA",
            "email": cls.email,
            "password": cls.password
        }
        create_response = requests.post(
            f"{cls.base_url}/Registration",
            json=user_payload,
        )

        cls.log.debug(f"'Registation' endpoint responded with {create_response.status_code} status code and {create_response.text}")

    def test_login(self):
        test_cases = [
            {
                "email": self.email,
                "password": self.password,
                "expected_status": 200,
                "expected_message": None
            },
            {
                "email": "wrong@email.com",
                "password": self.password,
                "expected_status": 200,
                "expected_message": "invalid username or password"
            },
            {
                "email": self.email,
                "password": "wrongpassword",
                "expected_status": 200,
                "expected_message": "invalid username or password"
            },
            {
                "email": "",
                "password": self.password,
                "expected_status": 400,
                "expected_message": "The request is invalid."
            },
            {
                "email": self.email,
                "password": "",
                "expected_status": 400,
                "expected_message": "The request is invalid."
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case):
                login_payload = {
                    "email": test_case["email"],
                    "password": test_case["password"]
                }
                login_response = requests.post(
                    f"{self.base_url}/Login",
                    json=login_payload,
                )
                
                self.assertEqual(login_response.status_code, test_case["expected_status"])
                self.log.debug(f"Test: {test_case}\nResponse: {login_response.text}")
                
                expected_message = test_case["expected_message"]
                response_json = login_response.json()
                
                if expected_message:
                    if "message" in response_json:
                        self.assertEqual(response_json["message"], expected_message)
                    elif "Message" in response_json:
                        self.assertEqual(response_json["Message"], expected_message)
                    else:
                        self.fail("Could not find 'message' or 'Message' key in the response.")

    @classmethod
    def tearDownClass(cls):
        # Clean up any test data or environment
        ...


if __name__ == '__main__':
    unittest.main()
