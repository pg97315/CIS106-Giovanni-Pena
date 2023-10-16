# Fibonacci sequence

a = 1
b = 1
c = 0

print(a)
print(b)

for i in range(1,19):
  c = a + b
  print(c)
  a = b
  b = c