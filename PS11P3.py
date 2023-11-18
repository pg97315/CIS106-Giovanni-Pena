#max an min

def find_max_min_index(scores):
  high_var = 0
  high_index = 0
  low_var = 100
  low_index = 0
  i = 0
  
  while i < len(scores):
    Qscore = scores[i]
    if Qscore > high_var:
      high_var = Qscore
      high_index = i
    if Qscore < low_var:
      low_var = Qscore
      low_index = i
    i = i + 1
  
  return high_index , low_index
  
text = open('names.txt' , 'r')
lines = text.readlines()

scores = []

for i in lines:
  score = i.split(",")
  score = int(score[1])
  scores.append(score)

max , min = find_max_min_index(scores)

print("Highest: " , lines[max] , "\nLowest: " , lines[min])