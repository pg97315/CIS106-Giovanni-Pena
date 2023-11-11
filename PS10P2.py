def det_average(score1 , score2, score3):
  global average, total_points
  average = (score1 + score2 + score3) / 3
  total_points = score1 + score2 + score3
  return average , total_points

name = input("Enter your last name: ")
score1 = float(input("Enter your first exam score: "))
score2 = float(input("Enter your second exam score: "))
score3 = float(input("Enter your third exam score: "))
print()

average , total_points = det_average(score1, score2, score3)

print(name, "the sum of your points is:" , total_points , "\nThe averga \
is:" , format(average , ".2f"))