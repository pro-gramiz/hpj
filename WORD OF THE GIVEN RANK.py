#question
You are given a word (String) 'S' and an integer representing the rank 'r', Your task is to permute through the string and arrange them in increasing order and say the word that is present in the index of 'r'.
Note: indexing starts from one
Input Format
Single line input contains a string 's' and an integer 'r' seprated by space
Constraints
1<=len(s)<=20
Output Format
single integer 'res'
Sample Input 0
CAB 2
Sample Output 0
ACB
Explanation 0
The possible permutations in lex order are,
1 ABC 2 ACB 3 BAC 4 BCA 5 CAB 6 CBA
The Word for rank 2 us ACB
************************************************************************************************************************************
#answer
from math import factorial as ft
def rep(n):
    s = set(n)
    res = 1
    for i in s:
        res = res * ft(n.count(i))
    return res
def least(n,k):
    ct = 0
    for i in n:
        if(i<k):
            ct += 1
    return ct
def rank(s):
    st = list(s)
    rank = 1
    n = len(st)

    for i in range(n):
        r = rep(st[i:])
        rank += (least(st[i:],st[i])*ft(n-i-1))//r
    return rank
