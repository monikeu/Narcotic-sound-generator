from random import randint

class questionManager:
    with open("questions", "r") as file:
        data = file.read()
    questions = data.split(",")
    length = len(questions)
    ifAsked = [] # was the question asked?

    def __init__(self):
        for i in range (0, self.length):
            self.ifAsked.append(False)

    def getRandomQuestion(self):
        random = randint(0, self.length-1)

        while self.ifAsked[random]:
            random = randint(0, self.length-1)
        self.ifAsked[random] = True
        return self.questions[random]
