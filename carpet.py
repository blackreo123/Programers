def solution(brown, yellow):
    answer = []
    all_brock = brown + yellow
    for i in range(1, all_brock):
       row = i
       col = all_brock / i

       if row > col:
           continue
       if (row-2)*(col-2) == yellow:
           answer.append(col)
           answer.append(row) 

    return answer

print(solution(24,24))