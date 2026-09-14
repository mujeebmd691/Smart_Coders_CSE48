# Calculate electricity bill based on slab rates
units = float(input("Enter units: "))
if units<=50:
    bill = 1*50
    print(f"Bill : Rs.{bill}")
elif 50<units<=100:
    bill = 1*50 + (units-50)*2
    print(f"Bill : Rs.{bill}")
elif 100<units<=150:
    bill = 50*1 + 50*2 + (units-100)*3
    print(f"Bill : Rs.{bill}")
elif 150<units<=200:
    bill = 50*1 + 50*2 + 50*3 + (units-150)*4
    print(f"Bill : Rs.{bill}")
else:
    bill = 50*1 + 50*2 + 50*3 + 50*4 + (units-200)*6
    print(f"Bill : Rs.{bill}")