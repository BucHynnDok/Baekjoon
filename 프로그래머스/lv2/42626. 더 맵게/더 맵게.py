from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    
    cnt = 0
    try:
        while scoville[0] < K:
            a = heappop(scoville)
            b = heappop(scoville)
            c = a + 2*b
            heappush(scoville,c)
            cnt += 1
    except:
        cnt = -1
    
    return cnt