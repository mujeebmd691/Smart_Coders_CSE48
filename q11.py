# Check if a number is even or odd using bitwise AND ( n & 1 )
n = int(input("Enter a number:"))
if n%2==0:
    print("Entered number is even.")
else :
    print("Entered number is odd.")

#method 2
a = [1, 2, 3, 4, 5]

res = map(lambda num: str(num) + " Even" 
          if num % 2 == 0 else str(num) + " Odd", a)

print("\n".join(res))

#method 3:
if n & 1 == 0:
    print("Entered number is even.")
else :
    print("Entered number is odd.")
