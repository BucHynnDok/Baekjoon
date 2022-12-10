import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
data = list(map(int,input().rstrip().split()))
cnt = [0] * m
data = data + [0]
for i in range(n):
    data[i] += data[i-1]
    cnt[data[i] % m] += 1

ans = cnt[0]

for i in cnt:
    ans += i*(i-1)//2

print(ans)