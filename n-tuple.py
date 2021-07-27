from ast import literal_eval

def solution(s):
    
    answer = []
    re_left = s.replace('{','[')
    re_right = re_left.replace('}',']')
    new_list = literal_eval(re_right)

    if len(new_list) == 1:
        answer.append(new_list[0][0])
    else:
        new_list.sort(key=len)
        for i in new_list:
            if len(i) == 1:
                answer.append(i[0])
            if len(i) > 1:
                answer.append(list(set(answer)^set(i))[0])
    
    
    print(answer)
    
    return answer




solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")