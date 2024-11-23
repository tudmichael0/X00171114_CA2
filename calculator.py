# calculator.py
# A simple calculator program that performs addition and subtraction


# Define a function to perform addition
def add(a, b):
    """Adds two numbers."""
    return a + b

"""
    Adds two numbers together.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
"""

# Define a function to perform subtraction
def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

"""
    Subtracts one number from another.
    :param a: First number
    :param b: Second number
    :return: Difference of a and b
"""

# Main program logic
if __name__ == "__main__":
# Provide instructions to the user
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")

# Input: Ask the user to choose an operation
    choice = input("Enter choice (1/2): ")
# Input: Get two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

# Input: Ask the user to choose an operation
    if choice == "1":
        print(f"The result is: {add(num1, num2)}")
    elif choice == "2":
        print(f"The result is: {subtract(num1, num2)}")
    else:
        print("Invalid choice")
