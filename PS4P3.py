# free shipping

price = int(input("What the price of the book that are you buying?: "))
print("")
quantity = int(input("How many books are you buying?: "))
print("")

total = float(price * quantity)

if total > 50:
  ship = 0
  print("Your total is: $" , total , "with free shipping.")
  
else:
  ship = 25
  print("Your total is: $" ,total + ship , "with $25 of shipping.")
  