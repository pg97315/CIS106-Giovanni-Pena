#I will do PS11P4 and P5 in the same code
def display_array(lnames , bats):
  i = 0
  print("Complete list of players: ")
  while i < len(lnames):
    print(lnames[i] , "= " , bats[i])
    i = i + 1
  print()

#This funtion is the PS11P5 (asking for a name)
def insert_lname(lnames , bats):
  selection = input("Enter the last name of the player: ")
  name_id = -1
  c = 0 

  while c < len(lnames):
    if lnames[c] == selection:
      name_id = c 
    c = c + 1

  if name_id == -1:
    print("Name no found")
  else:
    print("Player selected: " , lnames[name_id] , "\nBats average: " , bats[name_id])
    
#open file
text = open("batting.txt" , "r")
average_list = text.readlines()
lnames = []
bats = []

for word in average_list:
  lname , bat = word.split(" , ")
  bat = float(bat)
  lnames.append(lname)
  bats.append(bat)

#Start the program
start = input("Do you want to run this program (yes/no): ")
if start == "yes":
  display_array(lnames , bats)
  answer = input("Do you want to write a name: ")
  while answer == "yes":
    insert_lname(lnames , bats)
    answer = input("\nDo you want to enter another name? ")
  print("This program ends. ")
else:
  print("The program ends.")