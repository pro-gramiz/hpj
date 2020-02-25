from math import gcd as g
n=int(input())
l=list(map(int,input().split()))
i=0
temp_i=i
val=1
while(i<n):
    temp_i=i
    c=1
    while(l[i]-1!=temp_i):
        i=l[i]-1
        c+=1
    i=temp_i+1
    val=val*c//g(val,c)
print(val)
