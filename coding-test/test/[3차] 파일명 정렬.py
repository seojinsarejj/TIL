# 1차 --- 40.0 / 100.0
# import re
# def solution(files):
    
#     head = re.compile('\D+')
#     number = re.compile('[0-9]+')
    
#     for i in range(len(files)):
#         for j in range(len(files)-1-i):
            
#             check_head = head.findall(files[j])[0].lower() > head.findall(files[j+1])[0].lower()
#             check_number = int(number.findall(files[j])[0].lower()) > int(number.findall(files[j+1])[0].lower())
#             if check_head or check_number :
#                 files[j],files[j+1] = files[j+1],files[j]
                    
#     return files


# 2차 --- 성공
import re
def solution(files):
    
    head = re.compile('\D+')
    number = re.compile('\d+')
    
    for i in range(len(files)):
        for j in range(len(files)-1-i):
            
            check_head = head.findall(files[j])[0].lower() > head.findall(files[j+1])[0].lower()
            equal_head =  head.findall(files[j])[0].lower() == head.findall(files[j+1])[0].lower()
            check_number = int(number.findall(files[j])[0].lower()) > int(number.findall(files[j+1])[0].lower())
            if check_head :
                files[j],files[j+1] = files[j+1],files[j]
            elif equal_head and check_number :
                files[j],files[j+1] = files[j+1],files[j]
                    
    return files

# 다른 사람의 풀이
import re

def other_solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b