#question
Chess is a two-player strategy board game played on a checkered board with 64 squares arranged in an 8×8 grid. The game is played by millions of people worldwide. Pawn might take smaller steps but yet is considered to be one of the most powerfull coin. Since the pawns performed well in a particular war, they were given a promotion to bishop category. A Bishop is possible to move along any diagonal. "With greater power comes greater responsibilities" is a statement from the Spiderman movie, yet a line with great meaning. The Pawns wern't that much responsible with the newer power. They started fighting against eachother, so if any other pawn was in its path, they will attack each other.
Given a N * N grid, and a value P which specifies the number of pawns and followed by P values which specifies the position of those pawns(promoted to bishops). On our special chessboard, two pawns attack each other if they share the same diagonal. This includes pawns that have another pawn located between them, i.e. pawn can attack through pieces.
How many pair of attacks are possible?
Input Format
The first line of input has one integer value N The second line of input has one integer value P, which is the number of Pawns in the board Then it has P lines of inputs which has the indices of each Pawn who were promoted to Bishops.
Constraints
1<=N<=10^3 1<=P<=10^9 N - Size of the grid P - Number of Pawns
Output Format
One integer Output
Sample Input 0
2
2
0 0
1 1
Sample Output 0
1

***********************************************************************************************************************************
#answer
def check(k,i,j,n):
    temp_i = i
    temp_j = j
    
    m = 0
    #left_up
    while(temp_i-1>=0 and temp_j-1>=0):
        if(k[temp_i-1][temp_j-1]=='B'):
            m+=1
        temp_i-=1
        temp_j-=1
    temp_i = i
    temp_j = j
    #left_down
    while(temp_i+1<=n-1 and temp_j-1>=0):
        if(k[temp_i+1][temp_j-1]=='B'):
            m+=1
        temp_i+=1
        temp_j-=1
    temp_i = i
    temp_j = j
    #right_up
    while(temp_i-1>=0 and temp_j+1<=n-1):
        if(k[temp_i-1][temp_j+1]=='B'):
            m+=1
        temp_i-=1
        temp_j+=1
    temp_i = i
    temp_j = j
    #right_down
    while(temp_i+1<=n-1 and temp_j+1<=n-1):
        if(k[temp_i+1][temp_j+1]=='B'):
            m+=1
        temp_i+=1
        temp_j+=1
    return m

n = int(input())
#n = 5
k = [[0 for i in range(n)] for j in range(n)]
b_count = int(input())
for i in range(b_count):
    x,y = map(int,input().split())
    k[x][y] = 'B'
c = 0
for i in range(len(k)):
    for j in range(len(k[0])):
        if(k[i][j]=='B'):
            c = c + check(k,i,j,n)
print(c//2)
for i in k:
    print(*i)
