def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

#it stores the add and subtract functions
operations = [add, subtract]
a, b = 8, 2

 #use a loop to call each function
for func in operations:
  print(func(a, b))