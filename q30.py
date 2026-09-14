# Build a simple calculator (+, −, ×, ÷) using switch-case
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
operation = input("Enter your choice to perform calculation(1/2/3/4):")
match operation:
    case '1':
        print(f"sum of {a} and {b} is {a+b}")
    case '2':
        print(f"difference of {a} and {b} is {a-b}")
    case '3':
        print(f"product of {a} and {b} is {a*b}")
    case '4':
        print(f"Quotient when {a} is divided by {b} is {a//b}")
    case default:
        print("Invalid input.")


