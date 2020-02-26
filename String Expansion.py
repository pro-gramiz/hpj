import re
a=input()
num=re.compile('[\d]').findall(a)
alpha=re.compile('[\D]+').findall(a)
d=""
for i in range(len(alpha)):
    d=(alpha.pop()+d)*int(num.pop())
print(d)
