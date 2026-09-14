# Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)
from math import *
a,b,c = map(int,input("Enter the coefficients of x^2, x and constant orderly:").split())
D = (b**2)-(4*a*c)
if D>0:
    print("There are real and distinct roots for the equation.")
elif D==0:
    print("There are real and equal roots for the equation.")
else:
    print("There are imaginary roots for the equation.")
root1 = (-b + sqrt(D))/2*a
root2 = (-b - sqrt(D))/2*a
print(f"Root1 = {root1}. \nRoot2 = {root2}.")

