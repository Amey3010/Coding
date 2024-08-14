def FirstFactorial(num):
  if num == 0:
    return 1
  num *= FirstFactorial(num-1)
  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(input()))
