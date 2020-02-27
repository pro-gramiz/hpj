n,m=map(int,input().split(" "))
count=0
ans=0
while(m):
    if(m%2==1):
        ans+=n<<count
    count+=1
    m=m>>1
print(ans)


