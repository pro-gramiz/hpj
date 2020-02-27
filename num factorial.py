m,n=map(int,input().split())
i=2
c=0
l=[]
k=[]
while(n%i<n):
    n=n//i
    c=c+n
if(m==2):
    print(c)
else:
    for i in range(2,m):
        d=0
        while(m%i==0):
            d=d+1
            m=m//i
        if(d>=1):
            l.append(d)
    print(l)
    for i in l:
        s=c//i
        k.append(s)
    print(min(k))
    **************************************************************************************************************************************
    i/p:2 10
    o/p:8
