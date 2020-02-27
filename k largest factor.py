a=2
b=1
l=[]
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
l.sort(reverse=True)
if len(l)<b:
    print("error")
else:
    k=l[b-1]
    print(k)
