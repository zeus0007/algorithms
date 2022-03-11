class QA():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, answer_function):
        result = answer_function(self.question)
        if self.answer == result:
            print(self.question, '맞았습니다.')
        else:
            print(self.question, '틀렸습니다.')