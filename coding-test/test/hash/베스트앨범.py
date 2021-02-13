# 1차 --- 성공
def solution(genres, plays):
    
    genre = set(genres)
    
    plays_sum = []
    
    result = []
    
    for i in genre:
        genre_idx = [g for g in range(len(genres)) if i == genres[g]]
        play = [(j,plays[j]) for j in genre_idx]
        play.sort(key=lambda x : x[1],reverse=True)
        
        play_sum = sum([p[1] for p in play])
        play = [p[0] for p in play[:2]]
        plays_sum.append((i,play_sum,play))
        
    plays_sum.sort(key=lambda x : x[1],reverse=True)
    
    for i in plays_sum:
        result += i[2]
        
    return result
    