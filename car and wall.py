f,b,t,dis=map(int,input().split())
d=0
while(dis-b>0):
    d=d+f+b
    dis=dis-b+f
print((dis+d)*t)
#input
3 7 5 18
#output
180
