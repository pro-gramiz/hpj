m=10**9+7
def power(n,a):
    res=1
    while a!=0:
        if a&1:
            res=(res*n)%m
        a=a>>1
        n=(n*n)%m
    return res
t=int(input())
n=int(input())
print(t*power(2,n))
