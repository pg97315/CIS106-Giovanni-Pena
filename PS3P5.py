#Found the break even point

fixed = float(input("Enter the fixed cost: "))
print("")
price = float(input("Enter the price per unit: "))
print("")
cost = float(input("Enter the cost per unit: "))
print("")

breakPoint = round(float(fixed / (price - cost)),2)

print("The break even point is:" , breakPoint)