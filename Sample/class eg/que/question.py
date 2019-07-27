class Question:

    def __init__(self, question, a, b, c, d, ans):
        self.question = question
        self.a = a.strip()
        self.b = b.strip()
        self.c = c.strip()
        self.d = d.strip()
        self.ans = ans.strip()
    
    def check_ans(self, ans):
        if ans.upper() == self.ans:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.question}\nA.{self.a}\nB.{self.b}\nC.{self.c}\nD.{self.d}"
