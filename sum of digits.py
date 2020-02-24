n=list("TN-47-ae-7201")
l=[]
a=[]
for i in range(len(n)):
    if n[i].isdigit():
        l.append(n[i])
for i in range(len(l)):
    a.append(int(l[i]))
print(sum(a))
    

