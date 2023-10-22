#student credits

code = 0
extPrice = 0
total = 0

def det_district(code):
  if code == 'I':
    district = 250
  elif code == 'O':
    district = 550
  else:
    district = 0
  return district

def det_extended_price(district, quantity):
  extended_price = district * quantity
  return extended_price

ask = input("Do you want to run this program (yes/no): ")

while ask == 'yes':
  name = input("Enter your name: ")
  quantity = int(input("Enter the number of credits are you taking: "))
  code = input("Enter your district coude (I/O): ")

  district = det_district(code)
  extPrice = det_extended_price(district, quantity)
  print()
  
  print(name , "your tuition is $" , extPrice)
  total = total + extPrice
  ask = input("Do you want to run this program again (yes/no): ")
  print()

print()
print("Sum of all tuitions: $" , total)