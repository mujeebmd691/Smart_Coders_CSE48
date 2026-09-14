# Age Category : Classify a person as a child, teenager, adult, or senior based on age
age = int(input("enter your age:"))
if age<13:
    print("You are a child.")
elif 13<=age<=19:
    print("You are a teenager.")
elif 19<age<55:
    print("You are an adult.")
elif age>=55:
    print("You are a senior citizen.")
else:
    print("Invalid input.")