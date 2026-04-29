import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

no = input("Number of questions? (Has to be a integer)")
back = input("back? (Has to be a integer)")

questions = []
answers = []

clear_terminal()

for i in range(int(no)):
    n1 = random.randint(0,9)
    n2 = random.randint(0,9)
    sign = random.randint(0,1)
    if sign == 0:
        ans = n1 + n2
        questions.append(f"{n1} + {n2} = ")
        answers.append(ans)
    else:
        ans = n1 - n2
        questions.append(f"{n1} - {n2} = ")
        answers.append(ans)
        
        

def devilish_calulation(back):
    score = 0
    for i in range(len(questions)):
        print(f"{i+1}. {questions[i]}")
        if i < back:
            wait = input()
            clear_terminal()
            continue
            
        else:
            inputans = input(f"{i-back+1}. =")
            if inputans==str(answers[i-back]):
                score+=1
            clear_terminal()


    for i in range(back):
        a = input(f"{len(questions)-back+i+1}. =")

        
        if a==str(answers[len(questions)-back+i]):
                score+=1

    return score





print(f"your score is {devilish_calulation(int(back))}", end="")
print (f" out of {no}")

print(questions)
print(answers)

n = input("press any to quit")
