def solution(board, moves):
    answer = 0
    stack=[]
    #board[0]부터 가장 위에 쌓여서 board[len(board)-1]이 1층에 깔린다.
    #아니였다. board의 마지막부터~첫번째까지 역순으로 쌓인다. 문제가 더럽다.
    new_board=[[] for _ in range(len(board)+1)]
    
    for i in range(len(board)-1,-1,-1):
        for j in range(len(board[i])):
            if board[i][j]==0:
                continue
            new_board[j+1].append(board[i][j])
    for move in moves:
        try:
            temp=new_board[move].pop()
            stack.append(temp)
            if len(stack)>=2:
                if stack[-1]==stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer+=2
        except:
            continue
    return answer
