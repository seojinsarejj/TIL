def solution(s):
    # 완전 탐색

    answer = len(s)
    # aabbaccc
    for size in range(1, len(s) //2 + 1):
        # 압축은 문자열 길이의 절반까지만 판단하면 된다.
        count = 1
        compress = 0

        prev = s[:size] 
        # a
        for i in range(size, len(s) + size, size):
            # 1 ~ 8까지
            curr = s[i:i+size]
            s[1:2]
            if prev == curr:
                count +=1 
            else:
                compress += size + len(str(count)) if 1 <count else len(prev)
                prev = curr
                count = 1
        answer = min(answer, compress)

    
    return answer
