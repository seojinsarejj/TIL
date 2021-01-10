# 1차 --- 84.6 / 100.0
def solution1(phone_book):
    
    
    for i in range(len(phone_book)):
        for num in phone_book[i+1:]:
            if phone_book[i] in num:
                if num[:len(phone_book[i])] == phone_book[i]:
                    return False
                
    return True

# 2차 --- 성공
def solution2(phone_book):
    
    for i in range(len(phone_book)):
        for num in phone_book:
            if phone_book[i] != num and phone_book[i] in num:
                if num[:len(phone_book[i])] == phone_book[i]:
                    return False
                
    return True

# 다른사람의 풀이

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
