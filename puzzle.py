def solution(game_board, table):
    block = [[0 for _ in range(0,len(table))] for _ in range(0,len(table))]
    
    for i in range(0,len(table)):
        for j in range(0,len(table)):
            if table[i][j] == 1:
                block[i][j] = 1
                if table[i][j+1] != 1:
                    break
    for i in block:
        print(i)
    answer = -1
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])