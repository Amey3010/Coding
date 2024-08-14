#Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false

import re
def FindIntersection(strArr):
  d1 = [int(i) for i in re.split(",\s",strArr[0])]
  d2 = [int(i) for i in re.split(",\s",strArr[1])]
  strArr = []
  for i in d1:
    for j in d2:
      if i == j:
        strArr.append(i)
        break
      elif i < j:
        break
  if len(strArr) == 0:
    return False
  return strArr

# keep this function call here 
print(FindIntersection(input()))
