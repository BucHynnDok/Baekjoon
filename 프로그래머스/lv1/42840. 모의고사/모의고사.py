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
    answer = []
    for idx, x in enumerate(results):
        if x == max(results):
            answer.append(idx+1)
    return answer