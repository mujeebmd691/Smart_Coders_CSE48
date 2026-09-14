# Given 3 sides, check if a valid triangle can be formed
a,b,c = map(float,input("Enter 3 sides of a triangle:").split())
if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Triangle can be formed using provided values of sides.")
else:
    print("Triangle cannot be formed using these sides")