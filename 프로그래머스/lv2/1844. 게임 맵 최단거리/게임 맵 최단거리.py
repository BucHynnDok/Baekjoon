from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs(x,y):
        nonlocal n, m
        q = deque()
        q.append((x,y,1))
        while q:
            a, b, distance = q.popleft()
            
            if a == n-1 and b == m-1:
                return distance
            
            if maps[a][b] == 0:
                continue
            maps[a][b] = 0
            
            if a+1 < n:
                q.append((a+1,b,distance+1))
            if b+1 < m:
                q.append((a,b+1,distance+1))
            if a-1 >= 0:
                q.append((a-1,b,distance+1))
            if b-1 >= 0:
                q.append((a,b-1,distance+1))
        return -1
    return bfs(0,0)