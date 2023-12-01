# classes

class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@company.com"

  def bonus(self, rate):
    self.rate = float(rate)
    bonus = rate * self.pay
    return bonus

#I just try to do more things
name = input("Enter your first name: ")
last = input("Enter your last name: ")
pay = float(input("Enter your pay: "))

empl1 = Employee(name , last , pay)
print("")

print(empl1.email)
print(empl1.first , empl1.last)
print("First bonus: $" , empl1.bonus(.1))
print("Second bonus: $" ,empl1.bonus(.2))