Calculator Application

Overview

This is a basic Python calculator applicationm
Addition and subtraction are the key arithmetic operations it offers. 
My project's goal is to show basic ideas like automated testing, continuous integration (CI), and version control. 
For teaching reasons, this application aims to teach users how to integrate CI/CD pipelines with a basic Python software.


Technologies Used

Python: The primary programming language used for the application.

pytest: Testing framework used for unit testing the application.

flake8: Static code analysis tool for maintaining code quality.

GitHub: Source control platform to store the repository.

Azure DevOps: Used for automating the build, test, and deployment pipelines.

Visual Studio Code: Integrated development environment (IDE) used for coding.

Local Development Setup

First I entered visual studio code and made the calculator.py to act as the application.
I created a script to act as a basic calculator with the functions of addition and subtraction, 
I added comments to help me rememeber what does what and as well as an explaination if another coder were to look at my work.
Once this was done I tested to see if my code worked the way I intented it to using "python calculator.py".
It worked as desired so I made my first commit. I also added files for dependencies,unit testing,a .gitignore file and I also updated the calculator.py file as can be seen in my commits.

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