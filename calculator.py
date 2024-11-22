def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")

    choice = input("Enter choice (1/2): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"The result is: {add(num1, num2)}")
    elif choice == "2":
        print(f"The result is: {subtract(num1, num2)}")
    else:
        print("Invalid choice")
