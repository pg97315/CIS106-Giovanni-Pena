# part number and price

part = int(input("Enter the part number: "))
print("")
quantity = int(input("Enter the quantity: "))
print("")

price = 0

if part == 10 or  part == 55:
  price = 1
elif part == 99:
  price = 2
elif part == 80 or part == 70:
  price = 3
else:
  price = 5

totalcost = price * quantity

print("The No." , part , "has a price of: $" , price , "\nYour total is: $" , totalcost)