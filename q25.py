#given marks (0-100). Print grade. A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
marks = float(input("Enter marks:"))
if marks>=90:
    print("Grade: A")
elif 80<=marks<90:
    print("Grade: B")
elif 70<=marks<80:
    print("Grade: C")
elif 60<=marks<70:
    print("Grade: D")
else:
    print("Grade: F (or) Fail.")