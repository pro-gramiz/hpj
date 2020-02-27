m,f,g=map(int,input().split())
value=input().split("0")
c=0
for i in value:
    if i!="":
        c+=int(i,2)
if((c*f)<=m):
    print(c*f)
    print("escaped")
else:
    print("not escaped")
