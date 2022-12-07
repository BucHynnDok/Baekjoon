import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

n = int(input())
data = {}
for i in map(int,input().rstrip().split()):
    data[i] = 1

m = int(input())
for i in map(int,input().rstrip().split()):
    print(int(i in data))