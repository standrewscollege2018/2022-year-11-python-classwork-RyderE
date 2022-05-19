# setting up and connecting sqlite
import sqlite3

animalsdatabase = "colourDB.db"
coloursdatabase = "coloursdatabase.db"


# animals connection setup
connection1 = sqlite3.connect(animalsdatabase)
cursor = connection1.cursor()


# colours connection setup
connection2 = sqlite3.connect(coloursdatabase)
cursor2 = connection2.cursor()


# run program
run = "true"
# introduction
print("welcome to my quiz")
print("if you would like to do the quiz on faviorite animals type 1")
print("if you would like to do the quiz on faviorite colours type 2")
quiz_choice = input(" ")
if quiz_choice > "2":
    print("ERROR PLEASE RESTART PROGRAM")
    run = "false"

while run == "true":

    # getting name

    print("please enter you first name")
    name = input()

    # setting scores
    score1 = int(0)
    score2 = int(0)

    # if user picks animals quiz do this
    if quiz_choice == "1":
        print("welcome to the faviorite animals quiz")
        print("please type 1, 2, 3 or 4 to answer the questions")
        print("")

        # printing results
        cursor.execute(
            "SELECT question, answer_1, answer_2, answer_3, answer_4, correct_answer FROM favioritecolours"
        )
        results = cursor.fetchall()

        for result in results:
            print(f"{result[0]}")
            print(
                f"1. {result[1]:15}  2. {result[2]:15}  3. {result[3]:15} 4.{result[4]:15}"
            )
            # input and check correct answer
            animalsanswer = int(input())
            #

            if animalsanswer == result[5]:
                print("CORRECT!")
                print("")
                score1 = score1 + 1
            else:
                print("incorrect")
                print("")
        print("YOUR SCORE IS:")
        print(score1)

    # if user picks colours quiz do this
    if quiz_choice == "2":
        print("welcome to the faviorite colours quiz")
        print("please type 1, 2, 3 or 4 to answer the questions")
        print("")
        # printing results
        cursor2.execute(
            "SELECT question, answer_1, answer_2, answer_3, answer_4, correct_answer FROM colours"
        )
        results2 = cursor2.fetchall()

        for result in results2:
            print(f"{result[0]}")
            print(
                f"1. {result[1]:15} 2. {result[2]:15} 3. {result[3]:15} 4. {result[4]:15}"
            )
            # input and check correct answer
            coloursanswer = int(input())
            if coloursanswer == result[5]:
                print("CORRECT!")
                # updating score
                score2 = score2 + 1
            else:
                print("incorrect")
        # printing score
        print("YOUR SCORE IS")
        print(score2)
