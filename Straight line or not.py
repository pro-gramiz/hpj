x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
area=(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))//2
if area==0:
    print("Straight Line")
else:
    print("Not Straight Line")
