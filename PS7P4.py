#Inventary

sheet = open('sheet.txt' , 'r')
count = 0
totalOrder = 0

for line in open('sheet.txt'):
  name , quantity , price = line.split(',')
  quantity = int(quantity)
  price = int(price)
  extended_p = int(price * quantity)
  
  print(name , ': $' , price , '. Quantity: ' , quantity , 'Total: ' , extended_p)
  count += 1
  totalOrder = totalOrder + extended_p

print()
print('Sum of all: $' , totalOrder , '. Number of orders: ' , count , ". Average order: \
$" , totalOrder / count)