import sys
from collections import deque
sys.setrecursionlimit(1000000)
    


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    def bfs(r):        
        if visited[r] == 1:
            return 0
        visited[r] == 1
        q = deque()
        q.append(r)
        while len(q) != 0:
            u = q.popleft()
            for x in range(n):
                if computers[u][x] == 1 and visited[x] == 0:
                    visited[x] = 1
                    q.append(x)
        return 1
    
    for i in range(n):
        answer += bfs(i)
        
    return answer