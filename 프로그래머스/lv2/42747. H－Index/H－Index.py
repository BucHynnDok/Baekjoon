def solution(citations):
    citations.sort()
    n = len(citations)
    h_idx = []
    for h in range(1,n+1):
        s = 0
        for j in citations:
            if h <= j:
                s += 1
        if s >= h:
            h_idx.append(h)
    
    return h_idx[-1] if h_idx else 0