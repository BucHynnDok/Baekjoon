from heapq import heappush, heappop

def solution(operations):
    hmn = []
    hmx = []
    h = []
    for command in operations:
        if not h:
            while hmn:
                heappop(hmn)
            while hmx:
                heappop(hmx)
        
        if command[0] == 'I':
            heappush(hmn, int(command[2:]))
            heappush(hmx, (-int(command[2:]),int(command[2:])))
            heappush(h, int(command[2:]))
        elif command[0] == 'D':
            if h:
                if command[2] == '1':
                    heappop(hmx)
                    heappop(h)
                else:
                    heappop(hmn)
                    heappop(h)
            else:
                continue
                
        print(command,h,hmn,hmx)
    
    
    return[heappop(hmx)[1],heappop(hmn)] if h else [0,0]