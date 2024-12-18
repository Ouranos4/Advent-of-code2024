""""
This solution can work for 10-60 seconds. I'm unsure if
a more efficient solution exists. I think in C++ this would work for 1-2 seconds.
"""
import sys
sys.setrecursionlimit(1000000)
arr=[]
dirx = {'v':1,'<':0,'^':-1,'>': 0}
diry = {'v':0,'<':-1,'^':0,'>':1}
nxt={'v':'<','<':'^','^':'>','>':'v'}
cnt=0
lst=[]
def dfs(i,j,pos,vis):
    arr[i][j]='X'
    if(i==n-1 or i==0 or j==m-1 or j==0):
        return False
    if((i,j,pos) in vis):
        return True
    vis.add((i,j,pos))
    x,y=i+dirx[pos],j+diry[pos]
    if(arr[x][y]=='.' or arr[x][y]=='X'):
        return dfs(x,y,pos,vis)
    else:
        return dfs(i,j,nxt[pos],vis)


idi=0
idj=0
rot=''
with open("input.txt",'r') as f:
    j=0
    for i in f:
        arr.append([])
        for ch in i:
            if(ch!='\n'):
                arr[-1].append(ch)
            if(ch in '<^>v'):
                idi,idj,rot=j,arr[-1].index(ch),ch
        j+=1

n=len(arr)
m=len(arr[0])
res=0
dfs(idi,idj,rot,set())
for i in range(n):
    for j in range(m):
        if(arr[i][j]=='X'):
            arr[i][j]='#'
            if(dfs(idi,idj,rot,set())):
                res+=1
            arr[i][j]='X'
print(res)