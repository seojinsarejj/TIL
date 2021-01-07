# 1차 --- 정답
def solution(board, moves):
    
    stack=[0]
    new_board = []
    count = 0
    for i in range(len(board)):
        new_board.append([item[i] for item in board if item[i] != 0])
        
    for move in moves:
        if new_board[move-1] == []:
            continue
        item = new_board[move-1].pop(0)
        if item == stack[-1] :
            stack.pop()
            count += 2
        else :
            stack.append(item)

                
    return count


# 다른 사람의 풀이
def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer