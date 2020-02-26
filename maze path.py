import queue
def create_maze():
    l=[]
    l.append(["1","O","1","1","1","1","1"])
    l.append(["1"," ","1"," "," "," ","1"])
    l.append(["1"," ","1"," ","1"," ","1"])
    l.append(["1"," "," "," ","1"," ","1"])
    l.append(["1"," ","1","1","1"," ","1"])
    l.append(["1"," ","1"," ","1"," ","1"])
    l.append(["1"," ","1","1","1","x","1"])
    return l
def find_end(maze,moves):
    j=maze[0].index("O")
    i=0
    for move in moves:
        if move=="L":
           j-=1
        elif move=="R":
            j+=1
        elif move=="D":
            i+=1
        elif move=="U":
            i-=1
    if maze[i][j]=="X":
        print(moves)
        return True
    return False
n=queue.Queue()
n.put("")
add=""
directions=['L','R','U','D']
while():
    add=n.get()
    for j in directions:
        p=add+j
        if valid(maze,p):
            n.put(p)
maze=create_maze()
for i in maze:
    print(*i)
    
