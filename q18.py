# Find the largest of three numbers
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
c = int(input("Enter another number:"))
if a>b and a>c:
    print(f"{a} is largest.")
elif b>a and b>c:
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")