#ans
a=list(input())
x,y='',''
for i in a:
    if int(i)%2==0:
        y+=i
    else:
        x+=i
print(x+y)




#que
Write a program to arrange the odd digits first and even digits second of the given number.

Input Format

Input contains integer

Constraints

1 ≤ num ≤ 100000007

Output Format

Print the value

Sample Input 0

125732
Sample Output 0

157322
