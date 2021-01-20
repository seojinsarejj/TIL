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


