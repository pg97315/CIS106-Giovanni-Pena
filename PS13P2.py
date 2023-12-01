#my own object

class Student:

  def __init__(self, first, last, district, credits):
    self.first = first
    self.last = last
    self.district = district
    self.credits = credits

  def pay(self):
    global tuition
    if district == "I":
      tuition = credits * 250
    else:
      tuition = credits * 500
    return tuition

def display(Student):
  print("Name: " , first , last)
  print("Credits: " ,  credits)
  print("Total: $" , student1.pay())
    
first = input("Enter your first name: ")
last = input("Enter your last name: ")
district = input("Enter your district code (I/O): ")
credits = float(input("Enter how mnay credits are you enrollmented: "))
print("")

student1 = Student(first, last, district , credits)

display(Student)