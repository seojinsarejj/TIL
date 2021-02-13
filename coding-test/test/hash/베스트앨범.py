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
    

# 다른 사람의 풀이
def other_solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer