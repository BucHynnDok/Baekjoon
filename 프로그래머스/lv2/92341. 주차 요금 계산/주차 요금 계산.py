import math

def solution(fees, records):
    
    def cal_time(time1,time2):
        hours1, hours2 = int(time1[0:2]), int(time2[0:2])
        minutes1, minutes2 = int(time1[3:5]), int(time2[3:5])
        timediff = hours2*60 + minutes2 - hours1*60 - minutes1
        return timediff
    
    answer = []
    a = fees[0]; x = fees[1]
    b = fees[2]; y = fees[3]
    
    cars = {}
    results = []
    for i in records:
        time = i[0:5]
        num = int(i[6:10])
        state = i[11:13]
        if state == 'IN':
            cars[num] = time
        else:
            intime = cars[num]
            del cars[num]
            results.append((num,cal_time(intime, time)))
    for i in cars:
        intime = cars[i]
        results.append((i,cal_time(intime, '23:59')))
    
    print(results)
    
    tmp = {}
    for i in results:
        try:
            asdf = tmp[i[0]]
            tmp[i[0]] = asdf + i[1]
        except:
            tmp[i[0]] = i[1]
            
    
    answer = []
    for i in tmp:
        num, time = i, tmp[i]
        if time > a:
            fee = x + math.ceil((time-a)/b)*y
        else:
            fee = x
        answer.append((i,fee))
    print(answer)    
    answer.sort(key=lambda x:x[0])
    
    for i in range(len(answer)):
        answer[i] = answer[i][1]
    
    return answer