# Check if a triangle is equilateral, isosceles, or scalene given 3 sides
a,b,c = map(float,input("Enter 3 sides of a triangle:").split())
if a==c and b==c:
    print("Equilateral Triangle.")
elif a==c or b==c:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")