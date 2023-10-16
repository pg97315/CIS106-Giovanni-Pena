# student tuition

file = open("district_code.txt" , 'r')
total = 0
students = 0
price = 0
  
for line in file:
  name, code, credits = line.split( )
  credits = int(credits)
  if code == 'I':
   price = 250  
  else:
    price = 500
      
  tuition = credits * price
  total = total + tuition
  students += 1
  print(name , ':' , credits , 'credits' , ". Total: $" , tuition)
  
print()
print('Total tuitions: $' , total , "Total students: " , students)
  
file.close()