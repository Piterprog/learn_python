def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by 0 is not allowed."
    return a / b

def integer_division(a, b):
    if b == 0:
        return "Error: Division by 0 is not allowed."
    return a // b

def modulus(a, b):
    if b == 0:
        return "Error: Division by 0 is not allowed."
    return a % b

def power(a, b):
    return a ** b

print("-" * 30)
print("|   Hello, glad to see you!   |")
print("-" * 30)
print("\nChoose an option:")
print("  1 - Start")
print("  2 - Quit")
print("-" * 30)

while True:
    start = input("Enter your choice: ").strip()
    
    if start == "1":
        print("Okay, let's start!")
        break
    elif start == "2":
        print("Goodbye, see you later!")
        exit()
    else:
        print("Incorrect input, try again!")

print("\nChoose an operation:")
print("     { + }  { - }  { * }  { / }  { // }  { % }  { ** } ")

while True:
    choice = input("Enter operation: ").strip()
    if choice in ["+", "-", "*", "/", "//", "%", "**"]:
        break
    else:
        print("Incorrect operator, please enter one of { +, -, *, /, //, %, ** }")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

if choice == "+":
    result = plus(num1, num2)
elif choice == "-":
    result = minus(num1, num2)
elif choice == "*":
    result = multi(num1, num2)
elif choice == "/":
    result = division(num1, num2)
elif choice == "//":
    result = integer_division(num1, num2)
elif choice == "%":
    result = modulus(num1, num2)
elif choice == "**":
    result = power(num1, num2)

print(f"{num1} {choice} {num2} = {result}")
