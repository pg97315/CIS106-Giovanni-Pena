#calculate bonus

name = str(input("Enter your last name: \nLast name: "))
print("")

salary = float(input("Enter your salary: \nSalary: $"))
print("")
level = int(input("Enter your job level: \nJob Level: "))
print("")

bonus = 0

if level >= 10:
  bonus = .25
elif level > 5:
  bonus = .2
else: 
  bonus = .1
  
print(name , "your bonus is $" , salary * bonus)