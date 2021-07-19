def solution(priorities, location):
    answer = 0

    # 고유번호 매겨 놓기
    new_priorities = []
    for i in range(0,len(priorities)):
        new_priorities.append({i:priorities[i]})
    # print(new_priorities)

    # 첫번째꺼 꺼내서 비교해서 큰거 있으면 다시 넣기
    while True:
        poped = new_priorities.pop(0)
        for j in new_priorities:
            if list(j.values())[0] > list(poped.values())[0]:
                new_priorities.append(poped)
                poped = {"no" : "no"}
                # print(new_priorities) 
                break

        # 제일 큰거였을때 count 올리고 location이랑 고유번호랑 비교하기
        if list(poped.keys())[0] != "no":
            answer += 1
        if list(poped.keys())[0] == location:
            break
    return answer
print(solution([2, 1, 3, 2], 2))