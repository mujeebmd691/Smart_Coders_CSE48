# Convert temperature from Celsius to Fahrenheit and vice versa
celsius = float(input("Enter temp in celsius:"))
fahrenheit = (celsius*9/5)+32
print(f"The temp in fahrenheit is {fahrenheit}")
f = float(input("Enter temp in fahrenheit:"))
c = (f-32)*5/9
print(f"The temp in celsius is {c}")
