#5.2
from sortedcontainers import SortedSet
def check(l):
    for i in range(len(l)):
        for j in range(i):
            try:
                if(mp1[l[i]].count(l[j])):
                    return False
            except:
                pass
    return True
def fix(l):
    while(check(l)==False):
        for i in range(len(l)):
            for j in range(i):
                try:
                    if(mp1[l[i]].count(l[j])):
                        l.insert(i+1,l[j])
                        l.pop(j)
                except:
                    pass
    #print(l)
    return l

mp1={}
mp2={}
arr=[]
res=0
b=0

with open("input.txt",'r') as f:
    for i in f:
        t=1
        if '|'  not in i:
            t=0
        if(t):
            a=""
            b=""
            j=0
            while(i[j]!='|'):
                a+=i[j]
                j+=1
            j+=1
            while(j<len(i)):
                b+=i[j]
                j+=1
            a=int(a);b=int(b)
            if a not in mp1:
                mp1[a]= SortedSet([b])
            else:
                mp1[a].add(b)
        else:
            a=""
            j=0
            while j<len(i)-(i[len(i)-1]=='\n'):
                if(i[j]==','):
                    arr.append(int(a))
                    a=""
                else:
                    a+=i[j]
                j+=1
            try:
                arr.append(int(a))
            except:
                pass
            temp=arr.copy()
            arr=fix(arr)
            if(temp!=arr):

                res+=arr[len(arr)//2]
            arr.clear()
print(res)
