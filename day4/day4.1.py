#4.1
import sys
def check(s,i,j):
    if(s=="XMAS" or s=="SAMX"):
        print(i,j)
        return True
    return False
arr=[]
with open("input.txt", "r") as f:
    for i in f:
        arr.append(i)
res=0
for i in range(len(arr)-1):
    arr[i]=arr[i][:-1]
for i in range(len(arr)):
    for j in  range(len(arr[i])):
        if(j<len(arr[i])-3 and check(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3],i,j)):
            res+=1
        if(i<len(arr)-3 and check(arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j],i,j)):
            res+=1
        if(i<len(arr)-3 and j<len(arr[i])-3 and check(arr[i][j]+arr[i+1][j+1]+arr[i+2][j+2]+arr[i+3][j+3],i,j)):
            res+=1
        if(i<len(arr)-3 and j>2 and check(arr[i][j]+arr[i+1][j-1]+arr[i+2][j-2]+arr[i+3][j-3],i,j)):
            res+=1
print(res)

#4.2
import sys
def check(s,i,j):
    if(s=="MAS" or s=="SAM"):
        print(i,j)
        return True
    return False
arr=[]
with open("input.txt", "r") as f:
    for i in f:
        arr.append(i)
res=0
for i in range(len(arr)-1):
    arr[i]=arr[i][:-1]
for i in range(len(arr)):
    for j in  range(len(arr[i])):
        if(i<len(arr)-2 and j<len(arr[i])-2 and check(arr[i][j]+arr[i+1][j+1]+arr[i+2][j+2],i,j)):
            j+=2
            if(i<len(arr)-2 and j>1 and check(arr[i][j]+arr[i+1][j-1]+arr[i+2][j-2],i,j)):
                res+=1
            j-=2


print(res)