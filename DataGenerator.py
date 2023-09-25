import random
import datetime
char = ["a","A","C","4","0","P","E","i","7","3"]
boolean = [True,False]
string = ["Fishy","Minnow","Super T-spin Double!","Data Generator","Hellow World :)",":3"]
integer =[1,839191,303937,893,101,111111,38,8]
real = [1.09,9.8,7.008,1.000000000000000000002,839.029,1234567.09,753.5]
date = ["2023-09-25","2021-05-2099","2007-03-15","2010-07-29","2024-02-29"]
dataTypes = ["char","boolean","string","integer","real","date"]

def generateDatatype():
    dataType = random.choice(dataTypes)
    return dataType

questionAsked = 0
score = 0
while questionAsked < 20:
    startTime = datetime.datetime.now()
    dataType = generateDatatype()
    questionAsked += 1
    if dataType == "char":
        question = random.choice(char)
    elif dataType =="boolean":
        question = random.choice(boolean)
    elif dataType == "string":
        question = random.choice(string)
    elif dataType == "integer":
        question = random.choice(integer)
    elif dataType == "real":
        question = random.choice(real) 
    else:
        question = random.choice(date)
        
    for i in range(3):
        print(f"Data: {question}")
        answer = (input(("What is the data type? \n"))).lower()

        if answer == dataType:
            score += 1
            print("Correct \n")
            break
        print(f"Incorrect, {3-i-1} attempts left \n")

endTime = datetime.datetime.now()
timeTaken = endTime - startTime
print(f"You have answered 20 questions and scored a score of {score}/20. You took {timeTaken}")
