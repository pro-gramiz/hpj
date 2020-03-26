#ans
n=int(input())
a=list(map(int,input().split()))
print('YES' if sum(a)%2==0 and len(a)%2==0 else 'NO')




#que
In one operation you can choose two elements ai and aj (i≠j) and decrease each of them by one.You need to check whether it is possible to make all the elements equal to zero or not.

Input Format

The first line contains a single integer the size of the array. The second line contains n integers a1,a2,…,an the elements of the array

Constraints

1

Output Format

Print "YES" if it is possible to make all elements zero, otherwise print "NO".

Sample Input 0

4
1 1 2 2

Sample Output 0

YES

