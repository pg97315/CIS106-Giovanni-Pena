# calculate taxes

name = str(input("Enter your last name: "))
print("")
dependents = int(input("Enter the number dependents in your charge: "))
print("")
gross_income = float(input("Enter your gross income: "))
print("")

AGI = gross_income - (dependents * 12000)
income_tax = 0

if AGI <= 50000:
  income_tax = AGI * .1
  if income_tax < 0:
    income_tax = 100
  if AGI <= 0:
    AGI = 0

if AGI > 50000:
  income_tax = ((AGI - 50000) * .2 + 5000)
  
  
print(name , "your gross income is $" , gross_income)
print("With" , dependents , "depende\
nts, your adjusted gross income is: $" , AGI , "Your income tax is: $" , income_tax)