from question import Question

class QuestionManager:
    ques_list = []
    
    @classmethod
    def load_quiz(cls):
        with open("question.txt") as f:
            data = f.readlines()
            for line in data:
                q = line.split(',')
                cls.ques_list.append(Question(*q))

    @classmethod
    def begin_quiz(cls):
        cls.load_quiz()
        correct = 0
        wrong = 0
        for i,question in enumerate(cls.ques_list):
            print(f"{i}>{question}")
            ans = input("Enter the Choice alphabet :")
            if question.check_ans(ans):
                correct += 1
            else:
                wrong += 1
        
        QuestionManager.results(len(cls.ques_list),correct,wrong)

    @staticmethod
    def results(no,correct,wrong):
        rank = ['Dumb as a rock','Ah! you know something','Improve my friend','Almost there','Close to perfection','Legendery']
        print(f"No. of Questions : {no}")
        print(f"No. of Correct Answers : {correct}")
        print(f"No. of Wrong Answers : {wrong}")
        per = (correct/no)*100
        r = int(per)//20
        print(f"Percentage : {per}")
        print(f"Remarks : {rank[r]}")