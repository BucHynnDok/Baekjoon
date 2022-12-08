import heapq
import sys
input = sys.stdin.readline

n = int(input())

leftheap = []
rightheep = []
ans = []

for i in range(n):
    num = int(input())
    
    if len(leftheap) == len(rightheep):
        heapq.heappush(leftheap, (-num, num))
    else:
        heapq.heappush(rightheep, (num, num))

    if rightheep and leftheap[0][1] > rightheep[0][1]:
        min = heapq.heappop(rightheep)[1]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min, min))
        heapq.heappush(rightheep, (max, max))

    ans.append(leftheap[0][1])

print(*ans,sep='\n')

