#question
In a school, evryday morning at 8:00 AM sharp there will be a student gathereing when the principal will address the gathering. 2nd November 2019, it was almost yet another normal day, and the studetns were gathered for the morning assembly. But exactly at 8:05 AM the principal got a phone call from the chairman that the honourable president of India was nearby and due to come change in plans, he is going to visit the school in less than 10 minutes. 10 minutes of time is a very less time to organise the students, because it will look appealing only if the students were standing in sorted order. So Priya being the principal of the school, decided to remove certain students from gathering to make them stand in a sorted order. So help Priya to remove minimum number of students to make them stand in sorted order.
Input Format
First line of input has one integer input N and thee second line of input has N spaced integers, where N is the number of students and N spaced integers is the order inn which the students are standinng and each value corresponds to the height of a student
Constraints
1<=N<=10^9 1<=a[i]<=10^9 N - Number of students a[i] - Height of each students
Output Format
The minimum value integer which will be the number of people to be removed from the gathering to make the remaing people sorted.
Sample Input 0
6
1 2 3 9 4 5
Sample Output 0
1
***********************************************************************************************************************************
#answer
def lis(l,n,k):
    max = 0
    for j in range(1,len(l)):
        for i in range(j):
            if l[j]>l[i] and k[i]+1>k[j]:
                k[j] = k[i] + 1
                if max<k[j]:
                    max = k[j]
    #print("lis",max)
    return max
def lds(l,n,k):
    max = 0
    for j in range(1,len(l)):
        for i in range(j):
            if l[j]<l[i] and k[i]+1>k[j]:
                k[j] = k[i] + 1
                if max<k[j]:
                    max = k[j]
    #print("lds",max)
    return max

    
n = int(input())
l = list(map(int,input().split()))
k = [1 for i in range(n)]
a = n - lds(l,n,k)
b = n - lis(l,n,k)
#print(a,b)
print(a if a<b else b)

