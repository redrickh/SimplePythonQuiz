"""
for future kivy gui

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
# import stilus
"""


import random
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

"""We need one excel file(kerdesek.xlsx), then we will add quesiton from B1 column(B2,B3 etc...).
Our answer will be right below them. In this code we can write four answers down.
So it will look like something like this:
Question1  Question2  Question3
answer1    same1      same
answer2    ....       ....
answer3    ....       ....
answer4    same4      ....
"""


class Quizz:

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

