#Calculate forecast
def det_forecast_percent(month):
  global percent
  if month == "jan" or month == "feb" or month == "mar":
    percent = .1
  elif month == "apr" or month == "may" or month == "jun":
    percent = .15
  elif month == "jul" or month == 'aug' or month == 'sep':
    percent = .2
  else:
    percent = .25

  return percent

def det_next_month(sales , percent):
  global next_month
  next_month = sales * (1 + percent)

#loop

ask = input('Do you want to run this program? (yes/no): ')
print()
while ask == "yes":
  name = input("Enter your last name: ")
  month = input("Enter the first three letters of this month: ")
  det_forecast_percent(month)
  
  sales = float(input("Enter the sales of this month: $"))
  det_next_month(sales, percent)

  print()
  print("Sales of" , month , ": $" , format(sales , ".2f") , "\nSales of the next \
  month: $" , format(next_month , ".2f"))
  ask = input("\nDo you want to run this program again? (yes/no): ")

print("The programs ended.")