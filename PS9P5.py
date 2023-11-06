#house
total = 0
sum = 0
def det_assessed_value(county , value):
  global assessed_value
  if county == 'Cook':
    percent = .9
  elif county == "DuPage":
    percent = .8
  elif county == "McHenry":
    percent = .75
  elif county == "Kane":
    percent = .6
  else:
    percent = .7

  assessed_value = value * percent
  return assessed_value

ask = input("Do you want to run this program? (yes/no): ")

while ask == "yes":
  county = input("Enter the county name: ")
  value = float(input("Enter the market value of the house: "))
  assessed_value = det_assessed_value(county, value)
  print()
  print("The house in" , county , "county is $" , assessed_value)
  total = total + assessed_value
  sum = sum + value

  print()
  ask = input("Do you want to run this program again: ")
  
print("Total of all market values: $" , sum , "\nTotal of all the assessed values: \
$" , total)