def det_average(game1 , game2, game3, handicap):
  global average_final , average
  average = (game1 + game2 + game3) / 3
  average_final = average + handicap
  return average_final , average

name = input("Enter your last name: ")
game1 = float(input("Enter your scores. \nGame 1: "))
game2 = float(input("Game 2: "))
game3 = float(input("Game 3: "))
handicap = float(input("Enter the handicap: "))
print()

total , average = det_average(game1 , game2, game3, handicap)
print(name , "your average scores is " , average , "and your score with handicap \
is: " , average_final)