def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 빈 공간 표시용으로 0채우기
    bridge_now = [0] * bridge_length

    # 1초 동안 벌어지는 일들
    while len(bridge_now):
        answer += 1
        bridge_now.pop(0)
        
        if truck_weights:
            if sum(bridge_now) + truck_weights[0] <= weight:
                bridge_now.append(truck_weights.pop(0))
            else:
                bridge_now.append(0)

    return answer

print(solution(2, 10, [7,4,5,6]))