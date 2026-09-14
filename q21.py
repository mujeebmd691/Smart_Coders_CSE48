# Ticket Pricing : Calculate ticket price based on the customer's age.
age = int(input("Enter you age:"))
ticket_price = 0
if age<18:
    ticket_price = 2
    print(f"Ticket price is ${ticket_price}")
elif 18<=age<40:
    ticket_price = 3
    print(f"Ticket price is ${ticket_price}")
else:
    ticket_price = 4
    print(f"Ticket price is ${ticket_price}")