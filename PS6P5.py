# all your savings

discount = 0
savings = 0
sumS = 0

agree = input("Do you want to run this program: ")

while agree == "yes":
  quantity = int(input("Enter quantity:"))
  price = float(input("Enter price: "))
  print("")

  extended_price = price * quantity
  
  if extended_price > 10000:
    discount = .25
  else:
    discount = .10

  savings = price * discount
  discount_price = float(price - savings)
  
  print("Original price: $" , price * quantity , "\nDiscount: \
  $" , savings * quantity , "\nTotal:  $" , discount_price * quantity)

  sumS = savings * quantity + sumS
  
  print("")
  agree = input("Do you want to run this program: ")

print("")
print("Total savings: $" , sumS)