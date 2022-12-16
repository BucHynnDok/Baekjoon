from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    C = [ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    q = deque()
    answer = []
    for x in C:
        if q:
            if q[-1] < x:
                q.append(x)
                answer.append(1)
            else:
                answer[-1] += 1
        else:
            q.append(x)
            answer.append(1)
        
    return answer