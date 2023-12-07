# same class program
class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = float(pay) 
    self.position = position

  def bonus(self, rate):
    self.rate = float(rate)
    bonus = rate * pay
    return bonus 

#manager sub class
class Manager(Employee):
  def long_term_bonus(self):
    long_term = (pay * .4) + pay
    return long_term

first = input("Enter your first name: ")
last = input("Enter your last name: ")
pay = float(input("Enter your pay: "))
position = input("Are you a manager? (y/n): ")


#if statement
if position == "n":
  empl1 = Employee(first , last , pay)
  print(empl1.first , empl1.last)
  print("First bonus: $" , empl1.bonus(.1))
  print("Second bonus: $" ,empl1.bonus(.2))

else:
  empl1 = Manager(first , last , pay)
  print(empl1.first , empl1.last)
  print("Your bonus as manager: $" , empl1.long_term_bonus())