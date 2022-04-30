import pandas as pd
import ast
import random


"""We need one excel file(kerdesek.xlsx), then we will add questions from A1 to x1 columns (B1,C1 etc...).
Our answers will be right below them. The correct answer will always be in the second row(B2, C2 etc...). 
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


def result():
    print("-----------------------------")
    print("Végeredmény:")
    print("Helyes válasz:", good_guess)
    print("Rossz válasz:", wrong_guess)


class Main:

    def quiz(self):

        df = pd.read_excel("kerdesek.xlsx", engine="odf")  # reading our xlsx
        question_numbers = len(df.columns)  # column count in our xlsx
        question_number = int(question_numbers - 1)
        self.randomvalue = random.randint(0, question_number)  # random number between our column number

        with open("numbers.txt", "r") as c:
            x = c.readlines()  # read into a list
            x = [ast.literal_eval(x[i].rstrip('\n')) for i in range(len(x))]  # numbers in number.txt

        range_number = list(range(0, question_number + 1))  # making a list with all of our column numbers
        x.sort()
        while self.randomvalue in x:  # if the current random number is already in numbers.txt
            self.randomvalue = random.randint(0, question_number)  # making a new random number, until it doesn't
            if x == range_number:  # if every question asked, then
                result()
                new_game = input("""----------------------------- \nNincs több kérdés. Újra játszol? y/n: """)
                # asking if the user want to play again
                if new_game == "y":
                    self.guess_restart()
                    self.new_game()
                else:
                    exit()
                break

        random_column_listing = df.iloc[0:, self.randomvalue]  # choosing columns and listing
        random.shuffle(random_column_listing)  # randomize list
        correct_answer = pd.read_excel("kerdesek.xlsx", engine="odf")  # reading the correct answer from it (row 1)
        inputChoice = correct_answer.iloc[:, self.randomvalue].head(1).values  # correct answer in head(1)
        inputChoice = str(inputChoice).replace("[", "").replace("]", "").replace("'", "").replace("'", "")
        self.question_ask = random_column_listing  # randomized question list
        print("Lehetséges válaszok:---------")
        print(self.question_ask)  # Printing df2 var. random column list
        print("-----------------------------")
        choosing = str(input("Válasz: "))  # user input

        if choosing == str(inputChoice):  # if the inputChoice value is equal with user input, then
            print("Helyes válasz!")  # the answer is correct.
            self.already_asked()
            global good_guess
            good_guess += 1
            print("Helyes válasz:", good_guess)
            return build.quiz()
        else:
            self.already_asked()
            print("Rossz válasz. Helyes megoldás: " + inputChoice)  # wrong answer
            global wrong_guess
            wrong_guess += 1
            print("Hibás válasz:", + wrong_guess)
            if wrong_guess == 3:
                print("""-----------------------------
                Hármat hibáztál. Újra kell kezdened.""")
                wrong_guess = 0
                self.new_game()
            return build.quiz()

    def already_asked(self):
        self.save_it = open("numbers.txt", "a")  # new text file, where we save our random column numbers
        self.save_it.write(str(self.randomvalue))
        self.save_it.write("\n")
        self.save_it.close()

    def guess_restart(self):
        global wrong_guess
        wrong_guess = 0
        global good_guess
        good_guess = 0


    @staticmethod
    def new_game():  # clearing it
        txt = open("numbers.txt", "w")
        txt.write("")
        return


build = Main()
build.quiz()
