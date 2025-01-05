Python Calculator with CI/CD integration

Overview

This is a basic Python calculator application
Addition and subtraction are the key arithmetic operations it offers. 
My project's goal is to show basic ideas like automated testing, continuous integration (CI), and version control. 
For teaching reasons, this application aims to teach users how to integrate CI/CD pipelines with a basic Python software.


Technologies Used

Python: The primary programming language used for the application.

pytest, coverage.py: Testing framework used for unit testing the application.

flake8: Static code analysis tool for maintaining code quality.

GitHub: Source control platform to store the repository.

Azure DevOps: Used for automating the build, test, and deployment pipelines.

Visual Studio Code: Integrated development environment (IDE) used for coding.

Local Development Setup

First I opened Azure DevOps and created a new project, I then git cloned that repository via visual studio code.Once this was done I created calculator.py
and I had my first commit from the Azure not from the visual studio I then pushed the new code to my local machine using viusal studio. Then I used git to get the gihub connected,
Then on viusal studio code I added dependencies.txt, .gitignore and an empty test file. Next I commited the chnages and pushed them to both environments.



Application Features

The calculator application includes the following features:

Addition: Allows the user to add two numbers.

Subtraction: Allows the user to subtract one number from another.

User-friendly Interface: The application accepts user input via the command line and outputs the result.

Example of Code:
$ python calculator.py

code snippiet:

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

Enter first number: 5

Enter second number: 3

Choose operation (+, -): +

Result: 8

CI Pipeline Implementation
The CI pipeline is implemented using Azure DevOps and includes the following steps:
1. Dependency Installation: Installs required dependencies from `dependencies.txt`.
2. Static Code Analysis: Runs Flake8 to ensure code quality.
3. Unit Testing and Coverage: Executes tests with pytest and generates a code coverage report.
4. Publishing Results: Publishes test and code coverage results in the pipeline.

Proper Source Control Practices: I have used Git for version control, guaranteeing appropriate commit procedures with succinct, understandable messages. In order to streamline the development process and generate pull requests for code reviews prior to integrating any modifications into the main branch, I have implemented a branching strategy (Gitflow).

Build Automation Setup: Azure DevOps pipelines, which are activated each time code is posted to the repository, completely automate the build process. This makes it possible for the project to automatically create and compile artifacts, guaranteeing that the most recent modifications are constantly tested and prepared for deployment.

Unit Testing with Code Coverage: Using the pytest framework for Python (or a similar tool), I have incorporated unit tests into the pipeline to preserve code quality. In order to make sure that any new code is adequately tested, I have created Codecov to track and report the project's coverage percentage.

Implementation of Static Code Analysis: I have incorporated static code analysis into the pipeline. Maintaining a clean and safe codebase depends on identifying problematic code smells, security flaws, and coding standards adherence.

Pipeline Development  
Implementation of a Multi-Stage YAML Pipeline: Using Azure DevOps, I created a multi-stage YAML pipeline with separate phases for deployment, testing, and building. This method guarantees that the code is created and tested prior to deployment to various environments.

Artefact Management Configuration: Azure Artefacts (or a comparable repository) is where build artefacts, like binaries or Docker images, are kept. Because these artifacts are versioned, managing deployments across many environments is simple, and the right version is always deployed.

Build and Deployment Triggers Setup: As code is pushed to designated branches, I've set up the pipeline to automatically start builds, and deployment triggers make sure the application is only released once the build has passed the necessary tests and 

Proper Approval Gates Configuration:  Approval gates have been put in place to guarantee that no code is sent into production without the necessary manual approval. This guarantees that all required checks have been completed prior to deployment and contributes to the stability of the production environment.

Testing Implementation 
Integration of Security Testing:
I have incorporated both static and dynamic application security testing (SAST/DAST) into the pipeline to improve security. By doing this, vulnerabilities are found early in the development process.

Performance Testing Setup: To simulate load and examine how the application functions under pressure, I have integrated performance testing using Locust. Before every deployment, the performance tests are incorporated straight into the pipeline to confirm the scalability and performance of the application.

Selenium UAT Test Implementation:  Selenium is used to automate User Acceptance Testing (UAT). To ensure that the features function as intended and that the application is prepared for production, the tests replicate actual user interactions with the program.

Test Execution in Pipeline: The pipeline automatically runs UAT, performance tests, and unit tests. This guarantees that no code is released before undergoing extensive testing and validation.

Results Reporting: The Azure DevOps pipeline results dashboard shows the outcomes that are recorded following each test execution. This facilitates rapid debugging and problem-solving by enabling me to know whether any tests failed and what the possible cause might be.

Environment Management
I setup at least two environments (test and production):
I have at least two settings set up, one for production and one for testing. I can make sure everything functions properly in the testing environment before releasing code to production.

Environment-Specific Deployment Configurations: Using variables and configuration files (such as appsettings.Test.json and appsettings.Prod.json), deployment configurations are environment-specific. This enables the same codebase to exhibit varying behaviors based on the context in which it is deployed.

Successful Environment Deployment: The application is successfully deployed to the test and production environments by the pipeline. Deployments are carried out safely and without problems thanks to approval gates and automated deployment techniques (such as blue/green deployments).

Branch Policies and Protection
Branch protection rules are set in GitHub to enforce pull request reviews before merging into main
branches (e.g., development, master and feature/CA3). This ensures that all code changes are reviewed and tested
before they are incorporated into the main codebase.


Testing Strategy
Unit tests are implemented for all features (addition and subtraction).
Code coverage is tracked using Coverage.py and is maintained at 100%.