#Calculate the increase or decrease of shares prices

purchasePrice = float(input("Enter the original price of the shares: $"))
print("")

currentPrice = float(input("Enter the actual price of the shares: $"))
print("")

quantity = float(input("Enter the amount of shares you have: "))
print("")

finalPrice = round(float(currentPrice - purchasePrice),2)

if finalPrice > 0:
  print("You have earned: $" , finalPrice * quantity)

if finalPrice < 0:
  print("You have lost: $" , (finalPrice * quantity) * -1)

if finalPrice > 0:
  print("Your shares increase a:\
  " , round(float((finalPrice / purchasePrice) * 100),2) , "%")

if finalPrice < 0:
  negativePercent = round(float(finalPrice / purchasePrice)*100,2)
  print("Your shares decrease a:" , negativePercent * -1, "%")