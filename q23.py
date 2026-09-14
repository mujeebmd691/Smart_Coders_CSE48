# Time Greeting : Given an hour, print Morning, Afternoon, Evening, or Night.
hour = int(input("Enter current hour (24 hour format):"))
if 0<=hour<=24:
    if 5<=hour<12:
        print("Morning!")
    elif 12<=hour<16:
        print("Afternoon!")
    elif 16<=hour<20:
        print("Evening!")
    else:
        print("Night!!")
else:
    print("Invalid input.")