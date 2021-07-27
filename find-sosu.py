from itertools import permutations 
import math

def solution(numbers):
    answer = 0
    num_list = []
    permutation_list = []
    for i in numbers:
        num_list.append(i)
    
    for i in range(1, len(num_list)+1):
        permutation_list += list(permutations(num_list, i))

    combination_list = set([int(("").join(i)) for i in permutation_list])
    for i in combination_list:
        if i < 2:
            continue
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer
print(solution("011"))