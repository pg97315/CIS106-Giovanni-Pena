# fianl price of a car
sum = 0
count = 0
def det_percent_off(make, model, code):
  global percent
  if make == 'Honda' and model == "Accord":
    percent = .1
  elif make == "Toyota" and model == "Rav4":
    percent = .15
  elif code == "Y":
    percent = .3
  else:
    percent = .05
  return percent

def det_new_msrp(price, percent):
  global MSRP
  discount = price - (price * percent)
  MSRP = discount + (discount * .07)
  return MSRP
  
ask = input("Do you want to run this program? (yes/no): ")

while ask == 'yes':
  make = input("Enter the make of the car: ")
  model = input("Enter the model of the car: ")
  code = input("Enter the electric car code (Y/N): ")
  price = float(input("Enter the price of the car: "))

  percent = det_percent_off(make, model, code)
  MSRP = det_new_msrp(price , percent)
  sum = sum + MSRP
  count += 1
  print()
  print("The" , make , model , "is: $" , format(MSRP , ".2f"))
  print()
  ask = input('Do you want to run this program again:')

print()
if count == 1:
  print("The final price of the car is: $" , sum)
else:
  print("The sum of the" , count , "cars is: $" , sum)