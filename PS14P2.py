# own class
class Car:
  def __init__(self, make, model, price):
    self.make = make
    self.model = model
    self.price = float(price)
    self.discount = price * .9

class Sport(Car):
  def __init__(self, make, model, price):
    super().__init__(make, model, price)

  def options(self):
    self.extras = 0
    wheels = input("New sports wheels?: ")
    engine = input("New sport engine?: ")
    interior = input("New sport model interior?: ")
    if wheels == "yes":
      self.extras += 1000
    if engine == "yes":
      self.extras += 3000
    if interior == "yes":
      self.extras += 2000
    return self.extras

def program():
  make = input("Make: ")
  model = input("Model: ")
  price = float(input("Sticker price: $"))
  sport = input("Is it a sport car? (yes/no): ")
  print("")
  
  if sport == "no":
    car1 = Car(make, model, price)
    print("Your" , car1.make , car1.model , "has a 10% percent discount. Final price: \
  $" , car1.discount)
  else:
    car1 = Sport(make, model, price)
    print("Your sport" , car1.make , car1.model , "with all the extras features cost: \
  $" , price + car1.options())

program()