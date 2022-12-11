from collections import deque
import sys


def solution(queue1, queue2):
    q = queue1 + queue2
    target = sum(q)//2
    
    x, y = 0, len(queue1)
    curr = sum(q[x:y])
    cnt = 0
    
    while x < len(q) and y < len(q):
        
        if curr == target:
            return cnt
        elif curr < target:
            curr +=  q[y]
            y += 1
        else:
            curr -= q[x]
            x += 1            
        cnt += 1     
    
    return -1
            
    
    
   