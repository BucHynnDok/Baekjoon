from collections import deque

def solution(begin, target, words):
    visited = [False for i in range(len(words))]
    q = deque()
    q.append((begin,0))
    cnt = 0
    results = []
    while q:
        r, x = q.popleft()
        if r == target:
            results.append(x)
            break
        for v in words:
            if not visited[words.index(v)]:
                s = 0
                for i in range(len(r)):
                    if r[i] == v[i]:
                        s += 1
                if s == len(r)-1:
                    q.append((v,x+1))
                    visited[words.index(v)] = True
                    print(q)
        cnt += 1            
    if results:
        answer = results[0]
    else:
        answer = 0
    
    return answer