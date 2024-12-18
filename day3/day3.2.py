s = open("input.txt", 'r').read()
res=0
i=0
t=1
while (i<len(s)-3):
    if(s[i:i+4]=="do()"):
        t=1
        i+=3
    elif (s[i:i+7]=="don't()"):
        t=0
        i+=6
    elif(s[i:i+4]=="mul(" and t):
        i+=4
        a=""
        b=""
        while (i<len(s) and s[i].isdigit()):
            a+=s[i]
            i+=1
        if (i>=len(s) or s[i]!=','):
            continue
        i+=1
        while (i<len(s) and s[i].isdigit()):
            b+=s[i]
            i+=1
        if (i>=len(s) or s[i]!=')'):
            continue
        res+=int(t)*int(a)*int(b)
    i+=1

print(res)
