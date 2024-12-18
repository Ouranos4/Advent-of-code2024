s = open("input.txt", 'r').read()
res=0
i=0
while (i<len(s)-3):
    if (s[i:i+4]=="mul("):
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
        res+=int(a)*int(b)
    i+=1

print(res)
