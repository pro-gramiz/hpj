def primefactors(n):
    i = 2
    fac = []
    while i*i <=n:
        if n%i:
            i+=1
        else:
            n//=i
            fac.append(i)
    if n > 1:
        fac.append(n)
    return fac
x = int(input())
y = int(input())
fac = primefactors(y)
#print(fac)
rem_dup = list(set(fac))
ans = []
for i in rem_dup:
    temp = x
    sum = 0
    while(temp):
        temp//=i
        sum+=temp
    ans.append(sum//fac.count(i))
#print(ans)
print(min(ans))
***************************************************************************************************************************************
    i/p:10 2
    o/p:8
