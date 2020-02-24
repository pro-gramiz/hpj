a=input()
b=["#"]
for i in a:
    if i==b[-1]:
        b.pop()
    else:
        b.append(i)
if(len(b[1:])==0):
    print("-1")
else:
    print(*b[1:])
    
