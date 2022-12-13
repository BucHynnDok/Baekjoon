from collections import Counter

def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    s1, s2, s3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == supo1[i%5]:
            s1 += 1
        if answers[i] == supo2[i%8]:
            s2 += 1
        if answers[i] == supo3[i%10]:
            s3 += 1
    results = [s1,s2,s3]
    if max(results) == s1:
        if s1 != s2 and s1 != s3:
            answer = [1]
        elif s1 != s2 and s1 == s3:
            answer = [1,3]
        elif s1 == s2 != s3:
            answer = [1,2]
        elif s1 == s2 == s3:
            answer = [1,2,3]
    elif max(results) == s2:
        if s2 != s3:
            answer = [2]
        elif s2 == s3:
            answer = [2,3]
    else:
        answer = [3]
    return answer