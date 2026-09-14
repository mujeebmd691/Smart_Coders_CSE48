# Given 3 numbers, print them in ascending order using only if-else
a,b,c = input("Enter three numbers:").split()
if a<b and a<c:
    if b<c:
        print(f"{a}, {b}, {c}")
    else:
        print(f"{a}, {c}, {b}")
elif b<a and b<c:
    if a<c:
        print(f"{b}, {a}, {c}")
    else:
        print(f"{b}, {c}, {a}")
else:
    if b<a:
        print(f"{c}, {b}, {a}")
    else:
        print(f"{c}, {a}, {b}")

    