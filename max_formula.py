import re

def solution(expression):
    answer = 0
    # 1. + - *
    # 2. + * - 
    # 3. - + *
    # 4. - * +
    # 5. * + -
    # 6. * - +
    case1 = ['+', '-', '*']
    case2 = ['+', '*', '-']
    case3 = ['-', '+', '*']
    case4 = ['-', '*', '+']
    case5 = ['*', '+', '-']
    case6 = ['*', '-', '+']
    
    기호 = ['+', '-', '*']
    
    expression기호들 = re.findall('\D',expression)
    for i in 기호:
        expression = expression.replace(i,',')
    expression숫자들 = expression.split(',')
   
    for i in range(1, len(expression숫자들)+len(expression기호들),2):
        test_list1 = expression숫자들.insert(i,expression기호들[int((i-1)/2)])
        test_list2 = expression숫자들.insert(i,expression기호들[int((i-1)/2)])
        test_list3 = expression숫자들.insert(i,expression기호들[int((i-1)/2)])
        test_list4 = expression숫자들.insert(i,expression기호들[int((i-1)/2)])
        test_list5 = expression숫자들.insert(i,expression기호들[int((i-1)/2)])
        test_list6 = expression숫자들.insert(i,expression기호들[int((i-1)/2)])
    for i in case1:
        for j in range(0, len(test_list1)):
            if test_list1[j] == i:
                temp = str(eval(test_list1[j-1] + test_list1[j] + test_list1[j+1]))
                test_list1[j-1] = temp
                
                del test_list1[j]
                del test_list1[j]
                test_list1.append('^^')
                test_list1.append('^^')
                # print(expression숫자들)
        case1_res = test_list1[0]
    print(case1_res)
   
    for i in case2:
        for j in range(0, len(test_list2)):
            if test_list2[j] == i:
                temp = str(eval(test_list2[j-1] + test_list2[j] + test_list2[j+1]))
                test_list2[j-1] = temp
                
                del test_list2[j]
                del test_list2[j]
                test_list2.append('^^')
                test_list2.append('^^')
                # print(expression숫자들)
        case2_res = test_list2[0]
    print(case2_res)

    for i in case3:
        for j in range(0, len(expression숫자들)):
            if expression숫자들[j] == i:
                temp = str(eval(expression숫자들[j-1] + expression숫자들[j] + expression숫자들[j+1]))
                expression숫자들[j-1] = temp
                
                del expression숫자들[j]
                del expression숫자들[j]
                expression숫자들.append('^^')
                expression숫자들.append('^^')
                # print(expression숫자들)
        case3_res = expression숫자들[0]
    print(case3_res)

    for i in case4:
        for j in range(0, len(expression숫자들)):
            if expression숫자들[j] == i:
                temp = str(eval(expression숫자들[j-1] + expression숫자들[j] + expression숫자들[j+1]))
                expression숫자들[j-1] = temp
                
                del expression숫자들[j]
                del expression숫자들[j]
                expression숫자들.append('^^')
                expression숫자들.append('^^')
                # print(expression숫자들)
        case4_res = expression숫자들[0]
    print(case4_res)

    for i in case5:
        for j in range(0, len(expression숫자들)):
            if expression숫자들[j] == i:
                temp = str(eval(expression숫자들[j-1] + expression숫자들[j] + expression숫자들[j+1]))
                expression숫자들[j-1] = temp
                
                del expression숫자들[j]
                del expression숫자들[j]
                expression숫자들.append('^^')
                expression숫자들.append('^^')
                # print(expression숫자들)
        case5_res = expression숫자들[0]
    print(case5_res)

    for i in case6:
        for j in range(0, len(expression숫자들)):
            if expression숫자들[j] == i:
                temp = str(eval(expression숫자들[j-1] + expression숫자들[j] + expression숫자들[j+1]))
                expression숫자들[j-1] = temp
                
                del expression숫자들[j]
                del expression숫자들[j]
                expression숫자들.append('^^')
                expression숫자들.append('^^')
                # print(expression숫자들)
        case6_res = expression숫자들[0]
    print(case6_res)
    return answer

solution("100-200*300-500+20")