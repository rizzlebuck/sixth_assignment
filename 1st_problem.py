# Task 1
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def division(x,y):
    return x / y
def multiplication(x,y):
    return x / y

print(addition)
print(subtraction)
print(division)
print(multiplication)

# Task 2
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def division(x,y):
    return x / y
def multiplication(x,y):
    return x * y

def calculator():
    print("Basic calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

    choice = input("Enter choice: 1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    elif choice == "3":
        print(f'{num1} / {num2} = {division(num1, num2)}')
    elif choice == "4":
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    else:
        print( "Error: You have to pick (1/2/3/4).")

calculator()

# Task 3
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def division(x,y):
    if x == 0:
        return "Error: Cannot divide by 0"
    elif y == 0:
        return "Error: Cannot divide by 0"
    else:
        return x / y
def multiplication(x,y):
    return x * y

def calculator():
    print("Basic calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

    choice = input("Enter choice: 1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    elif choice == "3":
        print(f'{num1} / {num2} = {division(num1, num2)}')
    elif choice == "4":
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    else:
        print( "Error: You have to pick (1/2/3/4).")

calculator()
    