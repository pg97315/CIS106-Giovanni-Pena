#price and discount

def det_ext_price(quantity , price):
  ext_price = quantity * price

  if ext_price > 10000:
    discount = ext_price * .1
  else:
    discount = 0

  final_price = ext_price - discount
  return final_price

total = 0
answer = input("Do want to buy a product: (yes/no) ")

while answer == 'yes':
  quantity = int(input("Enter quantity: "))
  price = float(input("Enter the unit price: $"))
  print()

  ext_price = det_ext_price(quantity , price)
  print("Quantity: " , quantity , "\nUnit price: $" , price , "\nExtended price: \
  $" , ext_price)

  total = total + ext_price
  print()
  answer = input("Do want to add a product: (yes/no) ")
  print()

print()
print("Your total is: $" , format(total , ".2f"))