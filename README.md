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

Enter first number: 5

Enter second number: 3

Choose operation (+, -): +

Result: 8

CI Pipeline Implementation