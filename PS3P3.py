#Tip for meal

meal = float(input("Enter the total of the meal: "))
print("")

tip1 = round(float(meal * .15),2)
tipOne = round(float(meal + tip1),2)

tip2 = round(float(meal * .18),2)
tipTwo = round(float(meal + tip2),2)

tip3 = round(float(meal * .20),2)
tipThree = round(float(meal + tip3),2)

print("")
print("With 15% tip:")
print("")
print("Total: " , meal)
print("Tip: " , tip1)
print("Total with tip: " , tipOne)
print('''
''')

print("With 18% tip:")
print("")
print("Total: " , meal)
print("Tip: " , tip2)
print("Total with tip: " , tipTwo)
print('''
''')

print("With 20% tip:")
print("")
print("Total: " , meal)
print("Tip: " , tip3)
print("Total with tip: " , tipThree)