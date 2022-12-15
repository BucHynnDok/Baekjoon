from math import comb
def solution(clothes):
    h = {}
    for x in clothes:
        h[x[0]] = x[1]
    
    r = {}
    for x in h:
        if h[x] not in r:
            r[h[x]] = 1
        else:
            r[h[x]] = r[h[x]]+1
    
    answer = 1
    for x in r:
        answer *= r[x] + 1
        
    return answer-1