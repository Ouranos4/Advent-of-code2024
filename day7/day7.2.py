import sys
def rec(n,arr,curr,idx):
    if(idx==len(arr)):
        if curr==n:
            return True
        return False
    if(curr>n):
        return False
    return any((rec(n,arr,int(str(curr)+str(arr[idx])),idx+1),rec(n,arr,curr+arr[idx],idx+1),rec(n,arr,curr*arr[idx],idx+1)))

res=0
with open("input.txt",'r') as f:
    for i in f:
        n=""
        j=0
        while(i[j]!=':'):
            n+=i[j]
            j+=1
        n=int(n)
        j+=1
        arr=list(map(int,i[j:].split()))
        res+=(rec(n,arr,arr[0],1))*n
print(res)