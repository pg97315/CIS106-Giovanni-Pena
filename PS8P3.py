# calculate MPG

count = 0

def miles_gallon(miles, gallons):
  MPG = float(miles / gallons)
  return MPG

answer = input("Do you want to calculate a trip? (yes/no): ")

while answer == 'yes':
  destination = input("Enter destination city: ")
  miles = float(input("Enter number of miles travelled: "))
  gallons = float(input("Enter number of gallons used: "))
  print()

  MPG = miles_gallon(miles, gallons)
  count += 1 
  print("Destination: " , destination , "\nMiles: " , miles , "\nMPG\
  : " , format(MPG , ".1f"))
  answer = input("Do you want to calculate another trip? (yes/no): ")

print("Total of trips calculated: " , count)