#read text file

text = open('salaries.txt' , 'r')
total_bonus = 0

for line in open('salaries.txt'):
  last_name , salary = line.split(',')
  salary = float(salary)

  if salary >= 100000:
    bonus_r = .2
  elif salary >= 50000:
   bonus_r = .15
  else:
    bonus_r = .1

  bonus = salary * bonus_r
  total_bonus += bonus
  
  print(last_name , "Salary: $" , salary , "  Bonus: $" , bonus + salary)
text.close()

print()
print("Total bonus: $" , total_bonus)