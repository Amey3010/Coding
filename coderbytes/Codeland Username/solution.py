import re
def CodelandUsernameValidation(strParam):
  # code goes here
  #return (4<len(strParam)<25) and (re.match("[a-zA-Z]",strParam[0])) and (re.match("[a-zA-Z0-9_]",strParam)) and not (re.match("[_]",strParam[-1]))
  return re.search("^[A-Za-z][A-Za-z0-9_]{2,23}[A-Za-z0-9]$",strParam) != None

# keep this function call here 
print(CodelandUsernameValidation(input()))
