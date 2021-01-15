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

# def rep(m):
#     m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
#     return m
    

# def solution(m, musicinfos):
    
#     for music in musicinfos:
#         info = music.split(",")
#         start,end = info[0].split(":"), info[1].split(":")
#         time = int(end[1]) - int(start[1])
#         music = rep(info[3])
#         result = music * (time // len(music)) + music[:time % len(music)]
#         if rep(m) in result :
#             return info[2]
        
#     return None


# 3차 --- 90.0 / 100.0
# def rep(m):
#     m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
#     return m

# def get_time(start,end):
#     hour = int(end[0]) - int(start[0])
#     minit = int(end[1]) - int(start[1])
#     if minit < 0:
#         minit = 60 + minit

#     return hour * 60 + minit

# def solution(m, musicinfos):
    
#     for music in musicinfos:
#         info = music.split(",")
#         start,end = info[0].split(":"), info[1].split(":")
#         time = get_time(start,end)
#         music = rep(info[3])
#         result = music * (time // len(music)) + music[:time % len(music)]
#         if rep(m) in result :
#             return info[2]

#     return "(None)"

# 


# 4차 --- 93.3 / 100.0

# def rep(m):
#     m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
#     return m

# def get_time(start,end):
#     hour = int(end[0]) - int(start[0])
#     minit = int(end[1]) - int(start[1])
#     if minit < 0:
#         minit = 60 + minit

#     return hour * 60 + minit

# def solution(m, musicinfos):
    
#     dic = dict()
    
#     for music in musicinfos:
#         info = music.split(",")
#         start,end = info[0].split(":"), info[1].split(":")
#         time = get_time(start,end)
#         music = rep(info[3])
#         result = music * (time // len(music)) + music[:time % len(music)]
#         if rep(m) in result :
#             dic[time] = info[2]

#     if dic:
#         return dic[max(dic.keys())]   
    
#     return "(None)"


# 5차 --- 96.7 / 100.0
# def rep(m):
#     m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
#     return m

# def get_time(start,end):
#     hour = int(end[0]) - int(start[0])
#     minit = int(end[1]) - int(start[1])
#     if minit < 0:
#         minit = 60 + minit

#     return hour * 60 + minit

# def solution(m, musicinfos):
    
#     dic = dict()
    
#     for music in musicinfos:
#         info = music.split(",")
#         start,end = info[0].split(":"), info[1].split(":")
#         time = get_time(start,end)
#         music = rep(info[3])
#         result = music * (time // len(music)) + music[:time % len(music)]
#         if rep(m) in result :
#             if time not in dic.keys() :
#                 dic[time] = info[2]
 
#     if dic:
#         return dic[max(dic.keys())]   
    
#     return "(None)"



# 6차 --- 성공...!
from datetime import datetime
def rep(m):
    m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a").replace("E#","e")
    
    return m

def get_time(start,end):
    
    time = int((datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")).total_seconds() / 60)

    return time

def solution(m, musicinfos):
    
    dic = dict()
    
    for music in musicinfos:
        info = music.split(",")
        time = get_time(info[0],info[1])
        music = rep(info[3])
        result = music * (time // len(music)) + music[:time % len(music)]
        if rep(m) in result :
            if time not in dic.keys() :
                dic[time] = info[2]

    if dic:
        return dic[max(dic.keys())]   
    
    return "(None)"


print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))