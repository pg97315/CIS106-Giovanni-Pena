def det_commission(sales):
  global commission , next_year
  if sales > 100000:
    percent = .1
  else:
    percent = .05
  commission = sales * percent
  next_year = sales + (sales * .05)
  return commission , next_year

name = input("Enter your last name: ")
sales = float(input("Enter your sales: "))
commission , next_year = det_commission(sales)
print()
print(name , "your commission for theses sales is : $" , commission , "\nThe next year's target is: $" , next_year)