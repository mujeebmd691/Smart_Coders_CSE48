# Check if a number is positive, negative, or zero — then if positive check even/odd
n = int(input("Enter a number:"))
if n>0:
    if n%2==0:
        print("Entered number is positive and even.")
    else:
        print("Entered number is positive and odd.")
elif n==0:
    print("You entered zero.")
else:
    print("Entered number is negative.")