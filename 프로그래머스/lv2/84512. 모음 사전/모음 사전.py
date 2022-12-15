def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    
    results = []
    cnt = 0
    def dfs(a,x,visited):
        nonlocal cnt
        if ''.join(a) == word:
            results.append(cnt)
            return 
        if x == 5:
            return
        for i in range(5):
            a.append(alpha[i])
            cnt += 1
            dfs(a,x+1,visited)
            a.pop()
    dfs([],0,[False for _ in range(5)])
    return results[0]