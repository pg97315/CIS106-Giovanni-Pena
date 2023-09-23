# compute depend of the quantity

quantity = int(input("Enter the quantity of the product: "))
print("")

price = int()

if quantity > 1000:
  price = 3

if quantity < 1000:
  price = 5

extended_price = float(price * quantity)

print("For" , quantity , " to $" , price , " each. The total price \
is $", extended_price , ". Plus 7% of taxes is: \
$" , (extended_price * 0.07) + extended_price)