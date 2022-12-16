from collections import deque

def solution(s):
    q = deque()
    for x in s:
        if q:
            if x == '(':
                q.append(x)
            elif x == ')' and q[-1] == '(':
                q.pop()
            else:
                return False
        else:
            q.append(x)
    if q:
        return False
    
    return True