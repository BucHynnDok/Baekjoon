from collections import deque

def solution(rows, columns, queries):
    answer = []
    def rotate_rec(data,queries):
        min_results = []
        for r in queries:
            x1, y1, x2, y2 = r
            x1 = x1 - 1; y1 = y1 - 1
            x2 = x2 - 1; y2 = y2 - 1
            q = deque()
            for i in range(y1,y2):
                q.append(data[x1][i])
            for i in range(x1,x2):
                q.append(data[i][y2])
            for i in range(y2,y1,-1):
                q.append(data[x2][i])
            for i in range(x2,x1,-1):
                q.append(data[i][y1])
            
            min_results.append(min(q))
            
            q.rotate()
            
            for i in range(y1,y2):
                data[x1][i] = q.popleft()
            for i in range(x1,x2):
                data[i][y2] = q.popleft()
            for i in range(y2,y1,-1):
                data[x2][i] = q.popleft()
            for i in range(x2,x1,-1):
                data[i][y1] = q.popleft()
        
        return min_results
            
            
            
    def make_rec(rows,columns):
        data = [[0]*columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                data[i][j] = (i*columns + j + 1)
        return data
    
    
    
    return rotate_rec(make_rec(rows,columns),queries)