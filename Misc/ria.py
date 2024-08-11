# Ria's game where she turns any number into it's largest possible number by rearranging the digits.

def posi_pow(num,r):
    if r>=2:
        num *= posi_pow(num,r-1)
    elif r==1:
        return num
    elif r==0:
        return 1
    return num

def ria(inp):
    g = inp
    arr = []
    sum = 0

    while(g>0):
        s = g%10
        arr.append(int(s))
        g = int(g / 10)
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                arr[i] += arr[j]
                arr[j] = arr[i] - arr[j]
                arr[i] = arr[i] - arr[j]
    
    for i in range(len(arr)):
        sum += arr[i] * posi_pow(10,len(arr)-i-1)

    return sum

inp = int(input())
print(ria(inp))
