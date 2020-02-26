
def swap(n):
    for i in range(0,len(n)):
        if n[i]=="1" and n[i+1]=="0":
            n[i],n[i+1]=n[i+1],n[i]
            break
n=input().split()
rot=int(input())
for j in range(1,rot+1):
    if "".join(n).count('10')==0:
        break
    swap(n)
print(n)
   
