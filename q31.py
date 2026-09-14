# Read month number (1–12) and print number of days in that month
year = int(input("Enter year:"))
month = int(input("Enter month number (1-12):"))
match month:
    case 1:
        print(f"It's January {year}. There are 31 days.")
    case 2:
        if year%4==0:
            print(f"It's February, {year}. There are 29 days.")
        else:
            print(f"It's February, {year}. There are 28 days.")
    case 3:
        print(f"It's March, {year}. There are 31 days.")
    case 4:
        print(f"It's April, {year}. There are 30 days.")
    case 5:
        print(f"It's May, {year}. There are 31 days.")
    case 6:
        print(f"It's June, {year}. There are 30 days.")
    case 7:
        print(f"It's July, {year}. There are 31 days.")
    case 8:
        print(f"It's August, {year}. There are 31 days.")
    case 9:
        print(f"It's September, {year}. There are 30 days.")
    case 10:
        print(f"It's October, {year}. There are 31 days.")
    case 11:
        print(f"It's November, {year}. There are 30 days.")
    case 12:
        print(f"It's December, {year}. There are 31 days.")

        
