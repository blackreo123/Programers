from queue import PriorityQueue

def solution(scoville, K):
    answer = 0
    que = PriorityQueue()
    for i in scoville:
        que.put(i)
    
    while True:
        if que.qsize() < 2:
            if que.get() < K:
                answer = -1
                break
            else:
                break
        first = que.get()
        if first >= K:
            break
        second = que.get()
        mixed = first + (second * 2)
        answer += 1
        que.put(mixed)
    
    return answer





scoville = [1,2,3]
K = 11
print(solution(scoville, K))