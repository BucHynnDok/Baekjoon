import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

mx_heap = []

for i in range(n):
    if data[i] == 0:
        if len(mx_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(mx_heap)[1])
    else:
        heapq.heappush(mx_heap,(-data[i],data[i]))

