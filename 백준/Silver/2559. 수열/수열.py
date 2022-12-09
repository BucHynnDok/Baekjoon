import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())
data = list(map(int,input().rstrip().split()))

s = [sum(data[i] for i in range(k))]
for i in range(1,n+1-k):
    s.append(s[-1] + data[i+k-1] - data[i-1])

print(max(s))
