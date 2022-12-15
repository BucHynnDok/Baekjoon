from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    visited = [0 for _ in range(len(words))]
    results = []
    def dfs(x,r,target,words):
        if r == target:
            results.append(x)
        for v in words:
            if not visited[words.index(v)]:
                s = 0
                for i in range(len(v)):
                    if r[i] == v[i]:
                        s += 1
                if s == len(v)-1:
                    visited[words.index(v)] = 1
                    dfs(x+1,v,target,words)
                    visited[words.index(v)] = 0
                    
                    
    dfs(0,begin,target,words)
    print(results)
    if results:
        answer = min(results)
    else:
        answer = 0
    
    return answer