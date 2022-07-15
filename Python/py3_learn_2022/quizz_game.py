def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------")
        print(key)
        for i in options[question_num -1]:
            print(i)
        guess = input("Enter (A,B,C)")
        guess = guess.upper()
        guesses.append(guess) 
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses,guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct_guesses,guesses):
    print("----------------------")
    print("Results")
    print("----------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(guesses.get(i), end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is : "+ str(score)+"%")

def play_again():
    response = input("Do you wanna play again (yes/no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
questions = {
    "Who created Python?: " : "A",
    "What year was Pyjthon create: " : "B",
    "Python is tributed to comedy group?: ": "C",
    "Is the Earth round?:" : "A"
}
options = [["A. Carlos Mukoyi", "B. Elon Musk", "C. Qaqamba Mxinwa"],
          ["A. 1991", "B. 1996", "C. 1980"],  
          ["A. Carlos Mukoyi", "B. Elon Musk", "C. Qaqamba Mxinwa"],
          ["A. True", "B. False", "C. It is flat"]]
new_game()

while play_again():
    new_game()
print("Bye")