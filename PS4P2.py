# price by item

item = str(input("What do you want today? A) Fries B) Nuggets C) Burguer: "))
print("")
quantity = int(input("Enter how many do you whant: "))

if item == "A":
  price = 10

else:
  price = 20

extended_price = float(price * quantity)

print("")
print("The option" , item , "cost:" , price , ". Your total is: " , extended_price)