#tickets price

quantity = int(input("Enter the number of tickets: "))
print("")

price = 0

if quantity >= 25:
  price = 50
elif quantity > 10:
  price = 60
elif quantity > 5:
  price = 70
elif quantity < 5:
  price = 75

print("Quantity:" , quantity , "\nPrice: $" , price , "\nTotal: $" , quantity * price)