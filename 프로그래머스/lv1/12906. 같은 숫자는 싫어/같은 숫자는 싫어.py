from collections import deque

def solution(arr):
    q = deque()
    answer = []
    for x in arr:
        if q:
            if x == q[-1]:
                continue
            else:
                q.append(x)
        else:
            q.append(x)
    
    while q:
        answer.append(q.popleft())
                
    
    return answer