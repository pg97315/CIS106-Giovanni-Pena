#display names

names = ["Luna" , "Orion" , "Zeph" ,  "Stephany" , "Aria" , "Ahseen" , "Nova" , \
"Kairos" , "Azary" , "Sebastian"]

L = len(names)

def list_name(names):
  for i in names:
    print(i)

def reverse_list(names):
  for i in range(L-1,-1,-1):
    print(names[i])

print("Names in order: ")
list_name(names)
print("\nNames in reverse: ")
reverse_list(names)