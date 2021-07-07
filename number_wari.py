def solution(n):
    count = 0
    for i in range(1,n+1):
        a = 0
        for j in range(i,n+1):
            a = a+j
            if a == n:
                count =count + 1
    return count
print(solution(8))