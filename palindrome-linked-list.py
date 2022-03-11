# linked list가 팰린드롬 구인 판별
# 팰린드롬 구조 앞으로해도 뒤로 해도 똑같은 자료구조
from qa_system import QA

def answer_function(input_string):
    input_list = input_string.split('->')
    input_string = ''.join(input_list)
    back_string = input_string[::-1]

    if input_string == back_string:
        return 'true'
    else :
        return 'false'

qa1 = QA('1->2', 'false')
qa1.check_answer(answer_function)
qa2 = QA('1->2->2->1', 'true')
qa2.check_answer(answer_function)


