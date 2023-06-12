# Final Task:  API Testing with Python's requests library

Python scripts for testing specific API endpoints of the REST API located at [http://restapi.adequateshop.com/swagger/ui/index#](http://restapi.adequateshop.com/swagger/ui/index#). The API endpoints to be tested are:

1. POST `/api/AuthAccount/Login`
2. GET `/api/Tourist/{id}`


## Installation

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd AQASchool-Final`
3. Create a virtual environment (optional): `python3 -m venv venv`
4. Activate the virtual environment (optional):
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`

## Usage

Run the following command to execute all the tests:

   ```
   pytest
   ```

## Cleaning Up

TODO: ENV issue. Delete endpoint is unavailable

### CI/CD Pipeline Demonstration

**Demonstration of the CI/CD pipeline:**

- Pipeline Run: [Link to Pipeline Run](https://github.com/A-S-A-S/AQASchool-Final/actions/runs/5247623217/jobs/9478019885)
- Allure Report: [Link to Allure Report](https://a-s-a-s.github.io/AQASchool-Final/12/#)

![Pipeline Demonstration](https://i.imgur.com/FnpTb9w.png)

**Demonstration of the CI/CD pipeline with failed test:**

- Pipeline Run: [Link to Pipeline Run](https://github.com/A-S-A-S/AQASchool-Final/actions/runs/5247774303/jobs/9478370093)
- Allure Report: [Link to Allure Report](https://a-s-a-s.github.io/AQASchool-Final/15/#)

![Pipeline Demonstration with Failed Test](https://i.imgur.com/tJhPS93.png)
