import re
def CodelandUsernameValidation(strParam):
  # code goes here
  return (4<len(strParam)<25) and (re.match("[a-zA-Z]",strParam[0])) and (re.match("[a-zA-Z0-9_]",strParam)) and not (re.match("[_]",strParam[-1]))

# keep this function call here 
print(CodelandUsernameValidation(input()))
