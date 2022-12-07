import sys
input = sys.stdin.readline

n, c = map(int,input().rstrip().split())
location = [int(input()) for _ in range(n)]
location.sort()

min_distance = 1
max_distance = location[n-1] - location[0]

while(min_distance <= max_distance):
    mid = (min_distance + max_distance)//2
    idx = 0
    cnt = 1
    for i in range(n):
        if location[i] - location[idx] >= mid:
            cnt += 1
            idx = i
    if cnt < c:
        max_distance = mid -1
     
    else:
        min_distance = mid + 1        
        result = mid

print(result)
