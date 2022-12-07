import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline


n, c = map(int,input().rstrip().split())
data = [int(input()) for _ in range(n)]
data.sort()

#찾아야 할것은 최대로 가질 수 있는 '최소 거리'
# 거리를 탐색범위로 잡아야 한다. 
# '최대로 가질 수 있는'이므로 upper bound를 찾아야한다.

mn_d = 1
mx_d = data[n-1] - data[0]

while mn_d <= mx_d:
    mid = (mn_d + mx_d)//2
    idx = 0  # 가장 최근에 wifi를 설치한 좌표 0부터 시작
    cnt = 1  # 설치한 wifi 갯수 [0]에 설치하므로 1부터 시작
    for i in range(n):
        if data[i] - data[idx] >= mid:
            cnt += 1
            idx = i
    if cnt >= c:
        mn_d = mid + 1
        result = mid
    else:
        mx_d = mid - 1
                
print(result)

