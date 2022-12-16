from heapq import heapify, heappop, heappush

def solution(jobs):
    r, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for x in jobs:
            if start < x[0] <= now:
                heappush(heap, [x[1],x[0]])
        if len(heap) > 0:
            cur  = heappop(heap)
            start = now
            now += cur[0]
            r += now - cur[1]
            i += 1
        else:
            now += 1
        
    return r//len(jobs)