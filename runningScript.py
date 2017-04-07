from questionManager import questionManager
from subprocess import call

def getInput():
    answ = raw_input()
    while len(answ.split(" ")) != 1 :
        print("I SAID ONLY ONE WORD ANSWERS!!! \n"
              "Insert the answer again, this time CORRECTLY\n")
        answ = raw_input()
    return answ

manager = questionManager()
answers = []

print("\nHello! \nMy name is Narconatorrrr - narcotic sounds generator\n\n"
      "You wille be asked some questions in order to create a sound\n"
      "I'm picky, so I'll get angry if you will not follow the rules\n"
      "And the rules are: \n"
      "1. The answers should be one-word\n"
      "2. The level of narcoticness shoul be between 0 and 10 (inclusive)\n"
      "3. You can chose the path of output file. \n "
      "If you give me the name of existing file I'll overwrite it, so be carefull!\n"
      "Have fun! \n")

for i in range(0, 6):
    print(manager.getRandomQuestion())
    answers.append(getInput())

print("Now tell me the output file name with absolute path"
      "if you want it somwhere else than in current directory\n")
answers.append(getInput())

print("Choose the level of narcoticness:\n"
      "10 - the biggest, 0 - the lowest, but still kind of creepy:\n" )
answ = getInput()
while answ not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    print ("Level should be 0-10!\n"
           "Insert the answer again, this time CORRECTLY\n")
    answ = getInput()
answers.append(answ)


call(["python", "narkonatorrrr.py"] + answers)
print("Your file is ready!\n")



