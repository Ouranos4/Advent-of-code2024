import sys
sys.setrecursionlimit(100000)
arr=[]
dirx = {'v':1,'<':0,'^':-1,'>': 0}
diry = {'v':0,'<':-1,'^':0,'>':1}
nxt={'v':'<','<':'^','^':'>','>':'v'}
cnt=0
def dfs(i,j,pos):
    arr[i][j]='X'
    if(i==n-1 or i==0 or j==m-1 or j==0):
        return
    x,y=i+dirx[pos],j+diry[pos]
    if(arr[x][y]=='.' or arr[x][y]=='X'):
        dfs(x,y,pos)
    else:
        dfs(i,j,nxt[pos])


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
dfs(idi,idj,rot)
res=0
for i in arr:
    for j in i:
        if(j=='X'):
            res+=1
print(res)
