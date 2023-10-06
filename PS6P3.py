# average grades

count = 0
average2 = 0

agree = str(input("Do you want run this program: (yes/no)"))

while agree == "yes":
  name = str(input("Enter your last name: "))
  exam1 = float(input("Enter your first exam score: "))
  exam2 = float(input("Enter your second exam score: "))
  
  average = (exam1 + exam2) / 2
  count += 1 
  average2 += average

  print("")
  print(name , "your average score is:" , average)
  print("")
  print("")

  agree = input("Do you want to try again? (yes/no)")

print("Total of students:" , count , "\nThe total average is: " , (average2)/count)