Final Task: API Testing using Python's requests library 
Objective: Create tests for specific API endpoints of the REST API located at http://restapi.adequateshop.com/swagger/ui/index#. The API endpoints to be tested are: 
 
1. POST /api/AuthAccount/Login 
2. GET /api/Tourist/{id} 
 
Task Details 
1. For testing the POST /api/AuthAccount/Login endpoint, you are required to write test cases that cover different scenarios including: 
- Successful login 
- Unsuccessful login due to incorrect username/password 
- Unsuccessful login due to empty username/password 
- Other edge cases you deem necessary 
 
2. For testing the GET /api/Tourist/{id} endpoint, the task is more complex: 
- You should first create a new tourist using a relevant endpoint (for example, POST /api/Tourist). Ensure that you create a unique tourist and not modify or delete any existing tourist data. 
- After creating a tourist, write test cases to get the tourist data using the GET /api/Tourist/{id} endpoint. Scenarios you might consider: 
- Successful request 
- Tourist not found 
- Other edge cases you deem necessary 
 
You are expected to use Python's requests library for this task. Test cases should assert both HTTP status codes and response bodies where applicable. Don't forget to clean up any created data at the end of your tests to leave the environment as it was before the tests were run. 
 
Acceptance Criteria 
1. Sufficient test coverage for the POST /api/AuthAccount/Login and GET /api/Tourist/{id} endpoints. 
2. Clear and detailed reporting of each test case, including the purpose of the test, the expected result, and the actual result. 
3. Integration of your tests in a CI/CD pipeline. You are required to: 
- Create a GitHub repository for your code. 
- Integrate your repository with a CI/CD tool that runs your tests every time new code is pushed to the repository. 
- Provide a link to your repository and a demonstration of your pipeline in action. 
 
Note: To fulfill the CI/CD requirement, you will need to ensure your Python script can be run from the command line and will exit with a status code of 0 on success and non-zero on any failure. This allows the CI/CD tool to determine whether the tests passed or failed. 
 
Deliverables 
1. Python scripts for testing the above-mentioned API endpoints. 
2. Detailed reports for each test case. 
3. A GitHub repository containing your code. 
4. Demonstration of your CI/CD pipeline running the tests. 
 
Good luck and remember the aim of this task is not just to test the APIs but to understand how well they're working and to identify any potential issues.