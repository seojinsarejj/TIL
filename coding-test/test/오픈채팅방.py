# 1차 --- 성공
def solution(record):
    
    user = {}
    
    log = []
    
    for r in record:
        r = r.split()
        if r[0] == "Enter":
            user[r[1]] = r[2]
            log.append((r[1], "님이 들어왔습니다."))
        elif r[0] == "Leave":
            log.append((r[1], "님이 나갔습니다."))
        elif r[0] == "Change":
            user[r[1]] = r[2]
                
    result = [user[i] + j for i,j in log ]
    return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))