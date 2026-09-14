# Check if a character is uppercase, lowercase, digit, or special character

i = input("Enter a character:")

if i.isupper():
    print("Entered character is an uppercase character.")
elif i.islower():
    print("Entered character is a lowercase character.")
elif i.isdigit():
    print("Entered character is a digit.")
else:
    print("Entered character is a special character.")

