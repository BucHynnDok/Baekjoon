from collections import Counter 

def solution(participant, completion):
    a = set(participant)
    b = set(completion)
    if len(a) == len(b) + 1:
        c = a-b
        for i in c:
            return i
    else:
        a = Counter(participant)
        b = Counter(completion)
        c = a.most_common()
        for i in c:
            if b[i[0]] == a[i[0]] - 1:
                return i[0]
