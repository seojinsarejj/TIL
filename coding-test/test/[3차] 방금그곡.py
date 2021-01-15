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

# 2차 --- 56.7 / 100.0

def rep(m):
    m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
    return m
    

def solution(m, musicinfos):
    
    for music in musicinfos:
        info = music.split(",")
        start,end = info[0].split(":"), info[1].split(":")
        time = int(end[1]) - int(start[1])
        music = rep(info[3])
        result = music * (time // len(music)) + music[:time % len(music)]
        if rep(m) in result :
            return info[2]
        
    return None

print(solution2("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))