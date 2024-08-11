#Vendor's problem. calculate the least number of bills that amount to the price of the commodity or change.

def vendor(n,r=0):
    if n>=1000:
        r = vendor(n-1000,r+1)
    elif n>=500:
        r = vendor(n-500,r+1)
    elif n>=200:
        r = vendor(n-200,r+1)
    elif n>=100:
        r = vendor(n-100,r+1)
    elif n>=50:
        r = vendor(n-50,r+1)
    elif n>=20:
        r = vendor(n-20,r+1)
    elif n>=10:
        r = vendor(n-10,r+1)
    elif n>=5:
        r = vendor(n-5,r+1)
    elif n>=2:
        r = vendor(n-2,r+1)
    elif n>=1:
        r = vendor(n-1,r+1)
    return r

inp = int(input())
print(vendor(inp))
