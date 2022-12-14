def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    visited = [True for _ in range(n)]
    results = []
    def dfs(x,k):
        nonlocal n
        
        for i in range(n):
            if k >= dungeons[i][0]:
                if visited[i]:
                    visited[i] = False
                    results.append(x+1)
                    dfs(x+1,k-dungeons[i][1])
                    visited[i] = True
        return
    dfs(0,k)
    print(results)
    return max(results)