import re
from itertools import permutations 
def operation(a,op,b):
    a = int(a)
    b = int(b)
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
        
def solution(expression):
    # 세가지 연산자 + - *
    # 연산 우선순위 정할 수 있음
    # 길이가 3이상 100이하인 문자열
    # 연산자는 숫자와 숫자 사이에만
    # 숫자는 0~99
    # 최소 1개 연산자
    # 같은 연산자 끼리는 앞에 있는 것의 우선순위 높음
    splited = re.findall(r'([0-9]*)([+*-])([0-9]*)',expression)
    expression_list = []
    for t in splited:
        for c in t:
            if c != '':
                expression_list.append(c)

    # 우선 순위
    order = ['+','-','*']
    order_perm = list(permutations(order, 3))
    result = []
    ex_len = len(expression_list)
    for item in order_perm:
        copy_ex = expression_list.copy()
        for op in item:
            new_list = []
            for _ in range(ex_len):
                if copy_ex :
                    el = copy_ex.pop(0)
                else :
                    break
                if el == op:
                    past_num = new_list.pop()
                    next_num = copy_ex.pop(0)
                    new_list.append(operation(past_num,op,next_num))
                else :
                    new_list.append(el)
            copy_ex = new_list
            
        result.append(new_list)
    answer = [abs(x[0]) for x in result]
    answer = max(answer)
                
    return answer