#Task 1: Create functions for each arithmetic operation.

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    return a / b


#Task 2: Implement user input to receive numbers and an operation choice.

print("Please choose an operation (1/2/3/4)\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
operation = int(input(":"))

operand_left = float(input("Enter left operand:"))
operand_right = float(input("Enter right operand:"))


#Task 3: Ensure your program can handle division by zero and other potential errors.

if operation == 1:
    print(add(operand_left, operand_right))
elif operation == 2:
    print(subtract(operand_left, operand_right))
elif operation == 3:
    print(multiply(operand_left, operand_right))
elif operation == 4:
    try:
        print(divide(operand_left, operand_right))
    except ZeroDivisionError:
        print("Please stop trying to implode the universe.")
else:
    print("Choose a valid operation number from the list!")