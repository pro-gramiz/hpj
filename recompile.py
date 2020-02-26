import re
n=input()
num=re.compile('[\d]+').findall(n)
alpha=re.compile('[\D]+').findall(n)
s=""
for i in range(len(alpha)):
    s=(alpha.pop()+s)*int(num.pop())
print(s)
