def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot be divided by zero"
    else:
        return a / b

print("Simple Calculator")
print("Select Your Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice of 1, 2, 3, or 4: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    next_calculation = input("Would you like to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
