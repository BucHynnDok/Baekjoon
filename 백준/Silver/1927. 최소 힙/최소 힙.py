import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

mn_heap = []

for i in range(n):
    if data[i] == 0:
        if len(mn_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(mn_heap))
    else:
        heapq.heappush(mn_heap,data[i])

