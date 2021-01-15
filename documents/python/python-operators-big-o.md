# 파이썬 기본 연산자들의 시간 복잡도

## 리스트 타입 메소드

|     연산      |                      설명                       |         예제         |       복잡도       |              비고              |
| :-----------: | :---------------------------------------------: | :------------------: | :----------------: | :----------------------------: |
|     Index     |              n 번째 element에 접근              |         l[i]         |        O(1)        |                                |
|     Store     |              n 번째에 element 할당              |      l[i] = 10       |        O(1)        |                                |
|    Length     |               List의 길이 가져옴                |        len(l)        |        O(1)        |                                |
|    Append     |            List 뒤쪽에 element 추가             |     l.append(1)      |        O(1)        |                                |
|      Pop      |             List 뒤쪽 element 제거              |       l.pop()        |        O(1)        |                                |
|     Slice     |               List의 일부를 취함                |        l[a:b]        |       O(b-a)       | 복사되는 element의 개수에 비례 |
|    Extend     |            리스트뒤에 리스트를 붙임             | l.extend(other_list) | O(len(other_list)) | 추가되는 리스트의 size에 비례  |
|    Delete     |           특정 위치의 element를 제거            |      del l[10]       |        O(N)        |                                |
|  Containment  |       특정 element가 list내에 있는지 확인       | x in l , x not in l  |        O(N)        |       Searching Overhead       |
|    Remove     |             list에서 element를 제거             |     l.remove(20)     |        O(N)        |                                |
| Extreme Value |                 min/max 값 찾기                 |    min(l),max(l)     |        O(N)        |                                |
|   Iteration   |        리스트의 element들을 한번씩 순회         |    for item in l:    |        O(N)        |                                |
|     Sort      |                    정렬수행                     |       l.sort()       |      O(NlogN)      |                                |
|   Multiply    | 리스트의 element들을 k번 반복해서 리스트를 생성 |        k \* l        |     O(k \* l)      |                                |
