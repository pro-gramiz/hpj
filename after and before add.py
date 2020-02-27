i/p:3 10
o/p:[3]
2 3
2 3 4
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10



#answer
n,m=map(int,input().split())
l=[n]
print(l)
while(True):
    if(l[0]-1>0):
        l.insert(0,l[0]-1)
        print(*l)
    if(l[-1]+1<=m):
        l.append(l[-1]+1)
        print(*l)
    
