import re
def LongestWord(sen):
  pattern = "([^A-Za-z0-9])"
  s = re.split(pattern, sen)
  sen = s[0]
  for i in range(1,len(s)):
    if len(s[i]) > len(sen):
      sen = s[i]
  # code goes here
  return sen

# keep this function call here 
print(LongestWord(input()))
