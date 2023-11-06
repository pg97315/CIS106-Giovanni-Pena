# calculate the  tickect price
sum = 0
tickets = 0
def det_ticket_price(miles):
  global price
  if miles >= 30:
    price = 12
  elif miles >= 20:
    price = 10
  elif miles >= 10:
    price = 8
  else:
    price = 5

  return price

ask = input("Do you want to calculate the price ticket? (yes/no): ")
print()

while ask == 'yes':
  name = input("Enter your last name: ")
  miles = float(input("Enter the distance in miles from this station to Chicago: "))
  price = det_ticket_price(miles)
  sum = sum + price
  tickets += 1

  print("The price of this ticket is: $" , price)
  print()
  ask = input("Do you want to calculte the price of another ticket? ")

print("The total of" , tickets , "tickets is $" , sum)