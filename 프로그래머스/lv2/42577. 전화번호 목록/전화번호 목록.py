from itertools import combinations

def solution(phone_book):
    
    phone_book.sort()
    for idx in range(1,len(phone_book)):
        a = phone_book[idx-1] 
        b = phone_book[idx]
        if a in b[:len(a)]:            
            return False
    
    return True           
    