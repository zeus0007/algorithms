import time
class QA():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, answer_function):
        start_time = time.time()
        result = answer_function(self.question)
        end_time = time.time()
        run_time = (end_time - start_time)*1000
        if self.answer == result:
            print(f'''입력 : {self.question}\n답안 : {result}\n실행시간 : {run_time:.5f} ms\n맞았습니다.\n''')
        else:
            print(f'''입력 : {self.question}\n답안 : {result}\n실행시간 : {run_time:.5f} ms\n틀렸습니다.\n''')
        