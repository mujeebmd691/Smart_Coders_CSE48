# Check if a given character is an alphabet, digit, or special character
n = input("Enter a character:")
if n.isalpha():
    print("It's an alphabet.")
elif n.isdigit():
    print("It's a digit.")
else:
    print("It's a special character.")

'''other possible method:
m = input("Enter a character:")
if ('a'<= m <= 'z') or ('A' <= m <= 'Z'):
    print("It's an alphabet.")
elif ('0' <= m <= '9'):
    print("It's a digit.")
else:
    print("It's a special character.")'''