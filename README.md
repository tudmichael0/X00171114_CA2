Python Calculator with CI/CD integration

Overview

This is a basic Python calculator application Addition and subtraction are the key arithmetic operations it offers. My project's goal is to show basic ideas like automated testing, continuous integration (CI), and version control. For teaching reasons, this application aims to teach users how to integrate CI/CD pipelines with a basic Python software.

Technologies Used

Python: The primary programming language used for the application.

pytest, coverage.py: Testing framework used for unit testing the application.

flake8: Static code analysis tool for maintaining code quality.

GitHub: Source control platform to store the repository.

Azure DevOps: Used for automating the build, test, and deployment pipelines.

Visual Studio Code: Integrated development environment (IDE) used for coding.

Application Features

The calculator application includes the following features:

Addition: Allows the user to add two numbers.

Subtraction: Allows the user to subtract one number from another.

User-friendly Interface: The application accepts user input via the command line and outputs the result.

Example of Code: $ python calculator.py

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

CI Pipeline Implementation The CI pipeline is implemented using Azure DevOps and includes the following steps:

Dependency Installation: Installs required dependencies from dependencies.txt.
Static Code Analysis: Runs Flake8 to ensure code quality.
Unit Testing and Coverage: Executes tests with pytest and generates a code coverage report.
Publishing Results: Publishes test and code coverage results in the pipeline.
What I Learned:

How CI pipelines work in practice

Writing and running automated tests

Integrating quality checks into a development workflow

Using Git and Azure DevOps together in a real project

Understanding how DevOps practices improve reliability and consistency
