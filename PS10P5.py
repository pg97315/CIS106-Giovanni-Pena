def det_total(qty , unit_Price):
  global total , tax
  total = qty * unit_Price
  tax = total + (total * .07)
  return total , tax

qty = float(input("Enter the quantity of the item: "))
unit_Price = float(input("Enter the unit price: "))
total , tax = det_total(qty , unit_Price)
print()
print("Your total before tax is $" , total , "\nAfter tax is $" , tax)