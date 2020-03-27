#question
Given a string N and number of rotations K, rotate the fragments seperated by the vowels K times to the left hand side without bothering the postiion of the vowels.
Input Format
Frist line of input is a string input Second line of input is a integer input K, so rotate the string K times to the left side.
Constraints
3<=length of the string<=10^(10^7) 0<=K<=10^9
Output Format
Rotated string has to be printed
Sample Input 0
missing
1
Sample Output 0
ssingim
Explanation 0
m + i + ss + i + ng all the fragments of string - {m,ss,ng} will be rotated once to the left - {ss,ng,m} OUTPUT: ssingim
************************************************************
#answer
from re import *
s,n=input().split()
k='[a,e,i,o,u,A,E,I,O,U]+'
al=split(k,s)
x=int(n)%len(al)
for _ in range(x):
    al=al[1:]+al[:1]
v=findall(k,s)
res=al[0]
for i in range(1,len(al)):
    res+=(v[i-1]+al[i])
print(res)
