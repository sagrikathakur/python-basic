# Simple Calculator for Beginners
# Learning Concepts: Basic Math Operators, Functions, if-elif-else logic

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2

print("=== SIMPLE CALCULATOR ===")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {n1} + {n2} = {add(n1, n2)}")
        elif choice == '2':
            print(f"Result: {n1} - {n2} = {subtract(n1, n2)}")
        elif choice == '3':
            print(f"Result: {n1} * {n2} = {multiply(n1, n2)}")
        elif choice == '4':
            print(f"Result: {n1} / {n2} = {divide(n1, n2)}")
    except ValueError:
        print("Please enter valid numbers!")
else:
    print("Invalid choice!")
