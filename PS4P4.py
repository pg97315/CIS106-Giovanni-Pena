#percentage of warranty

name = str(input("Enter your name: "))
print("")
cost = float(input("Enter the cost of your appliance: $"))
print("")

percent = 0

if cost > 1000:
  percent = .1

if cost <= 1000:
  percent = .05

warranty = cost * percent

total = cost + warranty

print(name , "the cost of your appliance is:" , cost , "plus the warranty of\
 $" , warranty , "your total is $" , total)