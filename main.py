import random
import pandas as pd
import sys
import ast
sys.setrecursionlimit(10000)
pd.options.mode.chained_assignment = None  # default='warn'

"""We need one excel file(kerdesek.xlsx), then we will add questions from A1 to x1 columns (B1,C1 etc...).
Our answers will be right below them.The correct answer will always be the second row(B2, C2 etc...). 
We will shuffle them later, so it won't be in the same position when we print them to the user. 
In this code we can write four answers down.
So it will look like something like this:
Question1  Question2  Question3
Correct1    correct      same
answer2    ....       ...
answer3    ....       ....
answer4    answer4     ....
"""

wrong_guess = 0
good_guess = 0


class Main:

    def quiz(self):
        df = pd.read_excel("kerdesek.xlsx")  # reading our xlsx
        question_numbers = len(df.columns)
        question_number = int(question_numbers - 1)
        self.randomvalue = random.randint(0, question_number)

        with open("numbers.txt", "r") as c:
            x = c.readlines()  # read into a list
            x = [ast.literal_eval(x[i].rstrip('\n')) for i in range(len(x))]

        range_number = list(range(0, question_number + 1))
        x.sort()
        while self.randomvalue in x:
            self.randomvalue = random.randint(0, question_number)

            if x == range_number:
                new_game = input("Nincs több kérdés. Újra játszol? y/n: ")
                if new_game == "y":
                    self.new_game()
                else:
                    exit()
                break

        df2 = df.iloc[0:, self.randomvalue]  # choosing columns and listing
        random.shuffle(df2)  # randomize list
        df3 = pd.read_excel("kerdesek.xlsx")
        inputChoice = df3.iloc[:, self.randomvalue].head(1).values
        inputChoice = str(inputChoice).replace("[", "").replace("]", "").replace("'", "").replace("'", "")
        question_ask = df2  # randomized question list
        print("Válaszok:--------------")
        print(question_ask)  # Printing df2 var. random column list
        print("---------------------")
        choosing = str(input("Válasz: ")) # user input
        if choosing == str(inputChoice):  # if the inputChoice value is in the user input value, then the answer is correct
            print("Helyes válasz!")
            self.already_asked()
            global good_guess
            good_guess += 1
            print("Helyes válaszok:", good_guess)
            return build.quiz()
        else:
            self.already_asked()
            print("Rossz válasz. Helyes megoldás: " + inputChoice)
            global wrong_guess
            wrong_guess += 1
            print("Hibás válaszok:", + wrong_guess)

            return build.quiz()

    def already_asked(self):
        self.save_it = open("numbers.txt", "a")
        self.save_it.write(str(self.randomvalue))
        self.save_it.write("\n")
        self.save_it.close()

    def new_game(self):
        txt = open("numbers.txt", "w")
        txt.write("")
        return 


build = Main()
build.quiz()

