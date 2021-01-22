# 1차 --- 61.5 / 100.0
import re
def solution(str1, str2):
    
    c = re.compile("[a-zA-Z]{2}")
    
    str1_lst = [(str1[i]+str1[i+1]).upper() for i in range(len(str1)-1) if c.match(str1[i]+str1[i+1])]
    str2_lst = [(str2[i]+str2[i+1]).upper() for i in range(len(str2)-1) if c.match(str2[i]+str2[i+1])]
    
    a = len([i for i in str1_lst if i in str2_lst])
    b = len([i for i in str2_lst if i in str1_lst])
    
    insec = min(a,b)
    union = max(a,b)
    
    a = len([i for i in str1_lst if i not in str2_lst])
    b = len([i for i in str2_lst if i not in str1_lst])
    
    union += (a + b)
    if union == 0 :
        return 65536
    
    return int(insec/union * 65536)  