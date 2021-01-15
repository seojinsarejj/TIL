# 1차 --- 40.0 / 100.0
def solution1(m, musicinfos):
    
    for music in musicinfos:
        info = music.split(",")
        # time = 시간 구하기
        start,end = info[0].split(":"), info[1].split(":")
        time = int(end[1]) - int(start[1])
        during = len("".join(info[3].split("#")))
        result = info[3] * (time // during) + info[3][:time % during]
        if m in result :
            return info[2]
        
    return None


print(solution1("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))