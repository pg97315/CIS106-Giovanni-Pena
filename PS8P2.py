# average of hits and at bats

count = 0
total_average = 0
def get_average(bats, hits):
  average = (hits) / (bats)
  return average

answer = input("Do you want to enter a score (yes/no): ")

while answer == 'yes':
  name = input("Enter name: ")
  bats = int(input("Enter number of at bats: "))
  hits = int(input("Enter number of hits: "))
  print()
  average = get_average(bats, hits)
  print(name , "average: " , average)
  print()
  count += 1
  total_average = total_average + average

  answer = input("Do you want to enter another score? (yes/no): ")

print("Number of players: " , count , "\nAverage of all the playes\
: " , format(total_average / count , ".2f"))