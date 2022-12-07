import sys
import bisect

input = sys.stdin.readline

n = int(input())
dt = list(map(int,input().split()))

LIS = [dt[0]]
for i in range(1,n):
    if dt[i] > LIS[-1]:
        LIS.append(dt[i])
    else:
        a = bisect.bisect_left(LIS,dt[i])
        LIS[a] = dt[i]



print(len(LIS))