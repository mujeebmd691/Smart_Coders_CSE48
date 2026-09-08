# Calculate simple interest given P, R, T → (P × R × T) / 100
principle = float(input("enter the principle amount:"))
rate_int = float(input("Enter the rate of interest(percentage):"))
time_period = float(input("enter the time period in months: "))
s_interest = (principle*rate_int*time_period)/100
print(f"Simple Interest is {s_interest}")
