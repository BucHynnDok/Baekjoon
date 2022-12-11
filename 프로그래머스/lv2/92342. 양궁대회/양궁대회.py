max_num = -1
answer = []
                  

def solution(n, info):
    def cal_diff(apeach,ryan):
        score_r, score_a = 0, 0
        for i in range(11):
            if apeach[i] == ryan[i] == 0:
                continue
            if apeach[i] >= ryan[i]:
                score_a += 10-i
            else:
                score_r += 10-i
        return score_a, score_r
    

    def dfs(apeach,ryan,n,x):
        global max_num, answer
        if x == 11:
            a, r = 0, 0
            if sum(ryan) == n:
                a, r = cal_diff(info, ryan)
            elif sum(ryan) < n:
                ryan[-1] += n - sum(ryan)
                a, r = cal_diff(info, ryan)
            else:
                return
            if a < r:
                if max_num < r-a:
                    max_num = r-a
                    answer = [ryan[:]]
                elif max_num == r-a:
                    answer.append(ryan[:])
            return
        ryan.append(apeach[x]+1)
        dfs(apeach,ryan,n,x+1)
        ryan.pop()
        
        ryan.append(0)
        dfs(apeach,ryan,n,x+1)
        ryan.pop()
    
    dfs(info,[],n,0)
    if not answer:
        return [-1]
    for i in range(11):
        answer.sort(key=lambda x:x[i])    
    return answer[-1]