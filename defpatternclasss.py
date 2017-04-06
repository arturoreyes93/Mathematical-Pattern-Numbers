# creates a pattern of numbers
def pattern_1 (n):
  counter = 1
  while (counter <= n):
    num = 1
    while (num <= counter):
      print (num, end = ", ")
      num += 1
    counter += 1
    print ()
