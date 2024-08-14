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
