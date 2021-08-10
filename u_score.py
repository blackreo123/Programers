# a = [15, 14, 13, 11, 11]
# print(min(a))
# print(list(filter(lambda x: a[x] == min(a), range(len(a)))))
def solution(scores):
    answer = ''
    
    
    for i in range(0, len(scores)):
        score = []
        score_sum = 0
        for j in range(0, len(scores)):
            score.append(scores[j][i])
        print(score)
        if score[i] == max(score):
            if len(list(filter(lambda x: score[x] == max(score), range(len(score))))) < 2:
                score_sum = (sum(score) - score[i]) / (len(score) - 1)
                if score_sum >= 90:
                    answer = answer + 'A'
                elif score_sum >= 80 and score_sum < 90:
                    answer = answer + 'B'
                elif score_sum >= 70 and score_sum < 80:
                    answer = answer + 'C'
                elif score_sum >= 50 and score_sum < 70:
                    answer = answer + 'D'
                elif score_sum < 50:
                    answer = answer + 'F'
            else:
                score_sum = (sum(score)) / (len(score))
                if score_sum >= 90:
                    answer = answer + 'A'
                elif score_sum >= 80 and score_sum < 90:
                    answer = answer + 'B'
                elif score_sum >= 70 and score_sum < 80:
                    answer = answer + 'C'
                elif score_sum >= 50 and score_sum < 70:
                    answer = answer + 'D'
                elif score_sum < 50:
                    answer = answer + 'F'
        elif score[i] == min(score):
            if len(list(filter(lambda x: score[x] == min(score), range(len(score))))) < 2:
                score_sum = (sum(score) - score[i]) / (len(score) - 1)
                if score_sum >= 90:
                    answer = answer + 'A'
                elif score_sum >= 80 and score_sum < 90:
                    answer = answer + 'B'
                elif score_sum >= 70 and score_sum < 80:
                    answer = answer + 'C'
                elif score_sum >= 50 and score_sum < 70:
                    answer = answer + 'D'
                elif score_sum < 50:
                    answer = answer + 'F'
            else:
                score_sum = (sum(score)) / (len(score))
                if score_sum >= 90:
                    answer = answer + 'A'
                elif score_sum >= 80 and score_sum < 90:
                    answer = answer + 'B'
                elif score_sum >= 70 and score_sum < 80:
                    answer = answer + 'C'
                elif score_sum >= 50 and score_sum < 70:
                    answer = answer + 'D'
                elif score_sum < 50:
                    answer = answer + 'F'
        else:
            score_sum = (sum(score)) / (len(score))
            if score_sum >= 90:
                answer = answer + 'A'
            elif score_sum >= 80 and score_sum < 90:
                answer = answer + 'B'
            elif score_sum >= 70 and score_sum < 80:
                answer = answer + 'C'
            elif score_sum >= 50 and score_sum < 70:
                answer = answer + 'D'
            elif score_sum < 50:
                answer = answer + 'F'
    print(answer)
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))