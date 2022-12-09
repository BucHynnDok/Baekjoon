import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
A = [[0]*(len(s)) for i in range(26)]

for j in range(len(s)):
    A[ord(s[j])-97][j] += 1

sm_A = [[0]*(len(s)+1) for i in range(27)]

for i in range(1,27):
    for j in range(1,len(s)+1):
        sm_A[i][j] = sm_A[i][j-1] + A[i-1][j-1]

for i in range(q):
    alpha, l, r = input().rstrip().split()
    print(sm_A[ord(alpha)-97+1][int(r)+1]-sm_A[ord(alpha)-97+1][int(l)])

