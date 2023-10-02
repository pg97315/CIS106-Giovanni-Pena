# quantity of widgets

quantity = int(input("Enter quantity: "))
print("")

price = 0

if quantity > 10000:
  price = 10
elif quantity > 5000:
  price = 20
else:
  price = 30

extended_price = quantity * price

print("The price is: $" , extended_price , ". Plus a 7% of tax, the total \
is: " , ((extended_price * .07) + extended_price))