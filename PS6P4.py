# gross payment of differents employees

count = 0
sumG = 0
employees = []
payment = []

agree = str(input("Do you want to run this program? (yes/no): "))
print("")

while agree == "yes":
  name = str(input("Enter your last name: "))
  hour = float(input("Enter how many hours have you worked: "))
  rate = float(input("Enter how much is your pay rate: "))
  count += 1

  if hour <= 40:
    gross_pay = hour * rate
  else:
    gross_pay = ((hour - 40) * (rate * 1.5)) + (40 * rate)

  employees.append(name)
  payment.append(gross_pay)
  sumG += gross_pay
  print(name , "your pay is going to be: $" , gross_pay)
  print("")
  agree = input("Do you want to run this program again? (yes/no): ")

print("")
print(employees)
print(payment)
print("")

average2 = sumG / count
print("Total of employess:" , count , "\nTotal gross payment: $" , sumG , "\nThe \
average earned: $" , round(average2,2))