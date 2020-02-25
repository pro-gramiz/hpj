Pongal Festival, the first thing two things that come to our mind are holidays and sugarcane. So, it’s the time the sugarcane harvesters waited for. Jeevanantham is an amateur farmer trying to harvest some sugarcanes. Unlike others, he grew sugarcane in one straight line. Jeevanantham is a superstitious person, so he follows a certain pattern in cutting off the sugarcanes. Every other sugarcane he cuts next will be of lesser height than the one he cut previously and leaves the remaining uncut. So, what is the maximum number of sugarcanes can he sell for this Pongal?
Input Format
Given a number N followed by N spaced integers in the next line, where N is the number of sugarcanes and the n spaced integers will have the height of each sugarcane
Constraints
!<=N<=10^9 1<=a[i]<=10^9 N - number of sugarcanes a[i] - height of each sugarcane
Output Format
One single integer specifying the maximum number of sugarcanes that Jeevanantham can sell for this pongal
Sample Input 0
17
9 4 3 5 7 3 2 45 1 44 2 1 7 36 29 6 1
Sample Output 0
6

***********************************************************************************************************************************
#answer
l=list(map(int,input().split()))
k=[1 for i in range(len(l))]
for j in range(1,len(l)):
    for i in range(j):
        if l[j]<l[i] and k[i]+1>k[j]:
            k[j]=k[i]+1
print(max(k))
