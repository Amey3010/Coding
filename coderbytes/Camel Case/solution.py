'''
For this challenge, you will convert a string into camel case format.
You have the function CamelCase(str) that takes the str parameter being passed and returns it in proper camel case format where the first letter of each word is capitalized (excluding the first letter). The string will only contain letters and some combination of delimiter punctuation characters separating each word.
For example, if str is "BOB loves-coding, " your program should return the string bobLovesCoding.
'''
import re

def StringChallenge(strParam):
  pattern = re.compile("[^\w]")
  s = pattern.split(strParam.lower())
  c = ""
  for a in range(0,len(s)):
    if a == 0:
      c += s[a].lower()
    else:
      if len(s[a]) == 1:
        c += a.upper()
      else:
        c += s[a][:1].upper() + s[a][1:]
  return c
  #return re.sub(r'[3xq7pjuva5]', rep ,c) #special challenge in screenshot

def rep(m):
  return "--|" + m.group(0) + "|--"

inp = "cats AND*Dogs- are Awesome"
print(StringChallenge(inp))
