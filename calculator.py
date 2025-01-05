class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


def main():
    # Example usage of the Calculator class/ New comment for videos
    calc = Calculator()
    print("Addition: 2 + 3 =", calc.add(2, 3))
    print("Subtraction: 5 - 2 =", calc.subtract(5, 2))


# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
