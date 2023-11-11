def det_discount(price , dis_rate):
  global dis_amount
  global dis_price
  dis_amount = price * dis_rate
  dis_price = price - dis_amount
  return dis_amount, dis_price

qty = float(input("Enter the quantity of the item: "))
price = float(input("Enter the price of the item: "))
dis_rate = float(input("Enter the discount rate (decimals): " ))

dis_amount , dis_price = det_discount(price, dis_rate)

print()
print("The discount amount is: $" , dis_amount * qty, "\nThe total price is: \
$" , dis_price * qty)