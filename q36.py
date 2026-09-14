# Read the cost price and selling price — print profit, loss, or no profit no loss
cp = float(input("Enter the cost price:"))
sp = float(input("Enter the selling price:"))
if sp-cp > 0:
    print("There's a profit.")
elif sp-cp == 0:
    print("There's no profit no loss.")
else:
    print("There's a loss.")