import random
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

"""We need one excel file(kerdesek.xlsx), then we will add questions from B1 to x1 columns (B1,C1 etc...).
Our answers will be right below them.The correct answer will always be the second row(B2, C2 etc...). 
We will shuffle them later, so it won't be in the same position when we print them to the user. 
In this code we can write four answers down.
So it will look like something like this:
Question1  Question2  Question3
Correct1    correct      same
answer2    ....       ....
answer3    ....       ....
answer4    answer4     ....
"""


class Quiz:

    df = pd.read_excel("kerdesek.xlsx")  # reading our question and answers xlsx

    randomvalue = random.randint(1, 4)  # random number(from 1 to 4)
    df2 = df.iloc[0:, randomvalue]  # choosing Columns and listing
    random.shuffle(df2)  # randomize list

    df3 = pd.read_excel("kerdesek.xlsx")
    inputChoice = df3.iloc[0:, randomvalue].head(1) # choosing from the original column and also choosing the fist row(answer)
    question_ask = df2  # randomized questions list

    print("Válaszok:--------------")
    print(question_ask)  # Printing df2 var. random column list
    print("---------------------")
    choosing = str(input("Válasz: "))  # user input

    if choosing in str(inputChoice):  # if the inputChoice value is in the user input value, then the answer is correct
        print("Helyes")

    else:
        print("Helytelen")  # it wasn't correct whops

