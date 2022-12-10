def solution(numbers, target):
    answer = 0
    sm = 0 
    def dfs(x):
        nonlocal sm,answer,target
        if x == len(numbers):
            if sm == target:
                answer +=1
            return
        for i in range(2):
            if i%2 == 0:
                sm += numbers[x]
                dfs(x+1)
                sm -= numbers[x]
            else:
                sm -= numbers[x]
                dfs(x+1)
                sm += numbers[x]
    dfs(0)
    return answer