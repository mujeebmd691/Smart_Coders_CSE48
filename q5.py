# Divisibility Check : Check whether a 
# number is divisible by 3, 5, both, or neither.
num = int(input("Enter a number: "))
if num%3 == 0 and num%5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
elif num%3==0:
    print(f"{num} is divisible by 3 but not by 5.")
elif num%5==0:
    print(f"{num} is divisibel by 5 but not by 3.")
else:
    print(f"{num} is neither divisible by 5 nor by 3.")