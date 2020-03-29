#question
In an attempt to reveal the mysteries of human perception, Dr. Vaseegaran thought of conducting a small experiment. His associates will blindfold him and ue an equipment such that he will not be able to hear the surroundig noise. He will be made to walk for a certain distance in a straight line. After a certin point he will be made to turn ninety degerees either to let or right and continues to walk in the same direction and again cotinue to walk , and this continues for N times. After the halt, the blindfold will be removed and Dr. Vaseegaran has to answer how much far is the house is from him. So, How far is he from his home and in which direction?
Input Format
One line of spaced inputs, for example 3N - where 3 denotes the distance covered and N represents the direction in which he travells
Constraints
1<=length(string)<=10^9
Output Format
The distance from his point and his house and which direction
Sample Input 0
3N 4E
Sample Output 0
5.00SW

************************************************************************************************************************************
#answer1
from math import sqrt as sq
l1=list(map(str,input().split()))
l=[]
x=0
y=0
temp=0
for i in l1:
    if i =='N':
        x+=int(temp)
        temp=0
    elif i=='E':
        y+=int(temp)
        temp=0
    elif i=='S':
        x-=int(temp)
        temp=0
    elif i=='W':
        y-=int(temp)
        temp=0
    elif i!=' ':
        temp=temp*10+int(ord(i)-48)
result=sq(pow(x,2)+pow(y,2))
if x>0:
    l.append('S')
elif x<0:
    l.append('N')
if y>0:
    l.append('W')
elif y<0:
    l.append('E')
print("%.2f"%result,"".join(l))
*********************************************************************************************
#answer2
import math
a=input().split()
x,y=0,0
td=0
for i in a:
    td=td+int(i[:-1])
    if(i[-1]=="N"):
        y+=int(i[:-1])
    elif(i[-1]=="S"):
        y-=int(i[:-1])
    elif(i[-1]=="E"):
        x+=int(i[:-1])
    else:
        x-=int(i[:-1])
if(x==0 and y>0):
    way="S"
elif(x==0 and y<0):
    way="N"
elif(x>0 and y==0):
    way="W"
elif(x<0 and y==0):
    way("E")
elif(x>0 and y>0):
    way="SW"
elif(x<0 and y<0):
    way="NE"
elif(x<0 and y>0):
    way="SE"
elif(x==0 and y==0):
    way="You are at center"
else:
    way="NW"
dis=math.sqrt((x**2)+(y**2))
print("%.2f%s"%(dis,way))





