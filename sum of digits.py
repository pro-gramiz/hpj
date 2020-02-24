#answer1
n=list("TN-47-ae-7201")
l=[]
a=[]
for i in range(len(n)):
    if n[i].isdigit():
        l.append(n[i])
for i in range(len(l)):
    a.append(int(l[i]))
print(sum(a))

#answer2
import re
print(re.compile('[\d]').findall(input()))
l=[]
for i in range(len(a)):
    l.append(int(a[i]))
print(sum(l))



