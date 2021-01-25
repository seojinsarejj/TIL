# 1차 --- 성공
def solution(arr1, arr2):
    
    result = []
    
    for a in arr1:
        arr = []
        for b in range(len(arr2[0])):
            sum = 0
            for i in range(len(arr2)):
                sum += a[i] * arr2[i][b]
            arr.append(sum)
        result.append(arr)
        
    return result