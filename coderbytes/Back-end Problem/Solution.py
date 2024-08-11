import request
import json

def clean_data():
  #r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  r = requests.get('http://localhost/challenges/json/json-cleaning.json')
  k = r.json()
  return dic(k)

def dic(k):
  d = k
  if isinstance(k,dict):
    d = k.copy()
    for i in k.keys():
      if isinstance(d[i],dict) or isinstance(d[i],list):
        d[i] = dic(d[i])
      elif d[i] == "N/A" or d[i] == "" or d[i] == "-":
        d.pop(i,None)
  elif isinstance(k,list):
    d = k.copy()
    for j in range(0,len(d)):
      if isinstance(d[j],dict) or isinstance(d[j],list):
        d[j] = dic(d[j])
      elif d[j] == "N/A" or d[j] == "" or d[j] == "-":
        del d[j]
  return d
      
