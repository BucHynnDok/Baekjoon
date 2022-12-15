def solution(genres, plays):
    
    r = {}
    s = []
    for idx, x in enumerate(genres):
        if x not in r:
            r[x] = plays[idx]
        else:
            r[x] += plays[idx]
    
    for x in r:
        s.append((r[x],x))
    s.sort(reverse=True)
    answer = []
    for x in s:
        tmp = []
        for idx,y in enumerate(genres):
            if y == x[1]:
                tmp.append((plays[idx],idx))
        tmp.sort(key = lambda x:x[1])
        tmp.sort(key = lambda x:x[0] ,reverse=True)
        
        answer.append(tmp[0][1])
        if len(tmp) >= 2:
            answer.append(tmp[1][1])
    
    return answer