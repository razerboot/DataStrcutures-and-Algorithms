from collections import defaultdict,deque

def check(x,y,n,graph):
    if 0<=x<n and 0<=y<3 and y not in graph[x]:
        return True
    return False
def find_max(graph,moves,n):
    q = deque([(-1,1)])
    level = {}
    level_max=0
    level[str(-1)+"#"+str(1)]=0
    while(len(q)>0):
        if level_max==n:
            return level_max
        temp = q.pop()
        for move in moves:
            new_x = temp[0]+move[0]
            new_y = temp[1]+move[1]
            if check(new_x,new_y,n,graph):
                level[str(new_x)+"#"+str(new_y)]=level[str(temp[0])+"#"+str(temp[1])]+1
                if level_max<level[str(new_x)+"#"+str(new_y)]:
                    level_max = level[str(new_x)+"#"+str(new_y)]
                graph[new_x].add(new_y)
                q.append((new_x,new_y))
    return level_max

t = input()
moves = [(1,0),(1,1),(1,-1)]
graph = defaultdict(set)
while(t>0):
    n,q=map(int,raw_input().split())
    old_n=n
    graph.clear()
    while(q>0):
        x,y = map(int,raw_input().split())
        graph[x-1].add(y-1)
        #if graph[x-1]==set([0,1,2]):
        #    n=x
        #    break
        q-=1
    i=1
    while(i<n):
        if graph[i]==set([0,1,2]):
            n=i
            break
        elif graph[i]==set([1,2]):
            i+=1
            while(graph[i]==set([1]) or graph[i]==set([1,2])):
                i+=1
            if graph[i]==set([0,1]) or graph[i]==set([0,1,2]):
                n=i
                break
        elif graph[i]==set([0,1]):
            i+=1
            while(graph[i]==set([1]) or graph[i]==set([0,1])):
                i+=1
            if graph[i]==set([1,2]) or graph[i]==set([0,1,2]):
                n=i
                break
        i+=1
    print n
    t-=1
