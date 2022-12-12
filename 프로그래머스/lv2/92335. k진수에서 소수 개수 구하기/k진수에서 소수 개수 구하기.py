import math
def solution(n, k):
    num_k = []
    answer = 0
    while n > k:
        num_k.append(n%k)
        n = n//k
    num_k.append(n%k)
    num_k.reverse()
    
    def find_prime(x):
        if x == 1:
            return 0
        if x == 2:
            return 1
        for i in range(2,math.ceil(x**(1/2))+1):
            if x%i == 0:
                return 0
        return 1
    
    num_k = ''.join(map(str,num_k))
    
    idx_lst = [0]
    for i in range(len(num_k)):
        if num_k[i] == '0':
            idx_lst.append(i)
    
    print(idx_lst)
    print(num_k)
    results = []
    if len(idx_lst) > 1:
        for i in range(1,len(idx_lst)):
            if i == 1:
                    results.append(num_k[:idx_lst[i]])
                    continue
            if idx_lst[i] - idx_lst[i-1] != 1:
                results.append(num_k[idx_lst[i-1]+1:idx_lst[i]])
            if i == len(idx_lst)-1:
                if idx_lst[i] != len(num_k)-1:
                    results.append(num_k[idx_lst[i]+1:])
                
    else:
        results.append(num_k)
    
    print(results)
    answer = 0    
    for x in results:
        answer += find_prime(int(x))
        print(answer)
        
    return answer