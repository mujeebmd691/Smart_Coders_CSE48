# Check if a character is a vowel or consonant
a = input("Enter a character:")
if a in "aeiou":
    print("It is a vowel.")
elif a in "bcdfghjklmnpqrstvwxyz":
    print("It is a consonant.")
else:
    print("It is neither vowel nor consonant.")