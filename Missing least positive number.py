#ans
a=list(map(int,input().split()))
a.sort()
x=min(a)
if 1 not in a:
    print("1")
else:
    while(True):
        if x+1 in a:
            x+=1
        else:
            print(x+1)
            break
            
            
 
 #que
 Find the missing least positive number from the given array (size:6)

Input Format

Input contains array of integers

Constraints

1<=N<1000

Output Format

Print the missing least positive number

Sample Input 0

1 3 4 5 6 10

Sample Output 0

2

