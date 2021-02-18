def my_function2():
  start= 500
  end = 1000
  for i in range(start, end):
      for j in range(2, i):
          if (i % j) == 0:
              break
      else:
          print(i)

def my_function():
  start= 0
  end = 500
  for i in range(start, end):
      for j in range(2, i):
          if (i % j) == 0:
              break
      else:
          print(i)
  my_function2()
        
my_function()
