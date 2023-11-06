# calculate gallons of paint 
total_gallons = 0
def det_square_footage(L, W, H):
  global square_foot
  square_foot = (2 * L * W) + (2 * L * H) + (2 * W * H)
  return square_foot

def gallon_paint(square_foot):
  gallons = square_foot / 50
  return gallons

ask = input("Do you want to run this program? (yes/no)\n")
while ask == 'yes':
  L = float(input('Enter the lenght of the room: '))
  W = float(input("Enter the width of the room: "))
  H = float(input('Enter the height of the room: '))
  print()
  square_foot = det_square_footage(L, W, H)
  gallons = gallon_paint(square_foot)
  total_gallons = total_gallons + gallons
  
  print("The measurements of the room is " , square_foot , 'square feet' , "You will \
need" , format(gallons , '.0f') , "gallons of paint.")
  print()
  ask = input("You want to run this program again: ")
  print()

print()
print("The total of gallons for all the rooms are: " , format(total_gallons , '.0f'))