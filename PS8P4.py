#Employess gross payment

pay_rate = 0
count = 0
total = 0

def det_job_code(jobCode):
  if jobCode == 'L':
    pay_rate = 25
  elif jobCode == 'A':
    pay_rate = 30
  elif jobCode == 'J':
    pay_rate = 50
  else:
    pay_rate = 0
    
  return float(pay_rate)

def gross_payment(hours, pay_rate):
  grossPay = hours * pay_rate
  return grossPay

def gross_over_pay(hours, pay_rate):
  grossPay = (40 * pay_rate) + ((hours - 40) * (pay_rate * 1.5))
  return grossPay

ask = input("Do you want to compute a gross payment (yes/no): ")

while ask == 'yes':
  name = input("Enter your last name: ")
  jobCode = input("Enter your job code (L, A, J): ")
  hours = float(input("Enter your hours worked: " ))
  print()

  pay_rate = det_job_code(jobCode)

  if hours <= 40: 
    grossPay = gross_payment(hours, pay_rate)
  else:
    grossPay = gross_over_pay(hours, pay_rate)

  print(name, "your gross payment is: $" , grossPay)
  print()

  count += 1
  total = total + grossPay
  
  ask = input("Do you want to run this program again (yes/no): ")

print()
print("Number of people entered: " , count, "\nTotal of gross payments: $" , total)