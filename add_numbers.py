#!/usr/bin/env python3

def add_two_numbers(a, b):
    """Function to add two numbers."""
    return a + b

if __name__ == "__main__":
    # Example usage
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")