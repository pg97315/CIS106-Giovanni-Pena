#names and scores

names = ["Luna" , "Orion" , "Zeph" ,  "Stephany" , "Aria" , "Ahseen" , "Nova" , \
"Kairos" , "Azary" , "Sebastian"]

scores = ["89" ,	"73" , 	"93" , "79" ,	"91" , 	"99" , "97" ,	"83"	, "72" ,	"75"]

#they're parallel arrays, the amount of names are the same than scores
L = len(names)
c = 0

def list_order(names, scores):
  global c
  for i in range(L):
    c = c + 1
    print(c , ")", names[i], scores[i])

def list_reverse(names, scores):
  global L
  for e in range(L-1,-1,-1):
    L = L - 1
    print(L + 1, ")" , names[e], scores[e])

print("List in order: ") 
list_order(names, scores)
print()
print("List in reverse:")
list_reverse(names, scores)