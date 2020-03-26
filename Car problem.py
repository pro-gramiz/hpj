#ans
a=list(input())
while(len(a)>1):
    x=0
    for i in a:
        x+=int(i)
    a=list(str(x))
print('Valid' if a[0]=='1' or a[0]=='3' else 'Invalid')




#que
Balaji deva bought a new car and prefers certain registration numbers based on the following condition: The summation of the digits until he gets a number between 0 and 9 is expected to be 1 or 3. suggest whether the given inputs are Valid or not

Input Format

Input contains integer

Constraints

1<=N<=10000

Output Format

Print Valid or Invalid

Sample Input 0

1234

Sample Output 0

Valid


