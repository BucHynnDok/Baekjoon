from collections import deque

def solution(priorities, location):
    q = deque()
    s = deque()
    
    for i in range(len(priorities)):
        s.append((priorities[i],i))
        q.append(priorities[i])
    
    r = deque()
    while True:
        if s:
            if s[0][0] != max(q):
                s.rotate(-1)
                q.rotate(-1)
            else:
                tmp = s.popleft()
                if tmp[1] == location:
                    r.append(tmp)
                    break
                r.append(tmp)
                q.popleft()
        else:
            break
    
    return len(r)
    
    