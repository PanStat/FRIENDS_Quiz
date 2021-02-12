from tkinter import *
from qna import QAndA
import random
import time

with open("scores.txt", mode="r") as scores_file:
    HIGH_SCORE = scores_file.read()
YELLOW = "#FFFAA4"
BLUE = "#5EDFFF"
RED = "#FF4646"
GREEN = "#54E346"
BEIGE = "#E8E8E8"
FONT_NAME = "Forte"
FONT_NAME2 = "MV Boli"
score = 0
button_list = ["buttonA", "buttonB", "buttonC", "buttonD"]

def start_game():
    # TODO start timer
    buttonA.grid(column=0, row=3)
    buttonB.grid(column=1, row=3)
    buttonC.grid(column=0, row=4)
    buttonD.grid(column=1, row=4)
    start_game_button.grid_forget()
    next_turn()

def next_turn():
    current_q = QnA.q_list[QnA.question_num]
    question_label.config(text=current_q[0])
    numbers = [1, 2, 3, 4]
    random.shuffle(numbers)
    A, B, C, D = current_q[numbers[0]], current_q[numbers[1]], current_q[numbers[2]], current_q[numbers[3]]
    buttonA.config(text=f"{A}")
    buttonB.config(text=f"{B}")
    buttonC.config(text=f"{C}")
    buttonD.config(text=f"{D}")

def reset_all_buttons():
    buttonA.config(bg=BEIGE)
    buttonB.config(bg=BEIGE)
    buttonC.config(bg=BEIGE)
    buttonD.config(bg=BEIGE)
    next_question_button.grid_forget()


def next_quest():
    result_label.config(text="")
    reset_all_buttons()
    QnA.next_turn()
    next_turn()

def game_over():
    if score > int(HIGH_SCORE):
        with open("scores.txt", mode="w+") as file:
            file.write(str(score))

def check_correct(button_):
    global score
    correct = QnA.q_list[QnA.question_num][1]
    if button_['text'] == correct:
        button_['bg'] = GREEN
        result_label.config(text="Correct!", fg="green")
        score += 1
        score_label.config(text=f"Score: {score:02d}")
        next_question_button.grid(column=0, row=7, columnspan=2)
    else:
        button_['bg'] = RED
        result_label.config(text=f"Wrong! The correct answer is {correct}", fg="red")

def keypress_A():
    check_correct(buttonA)

def keypress_B():
    check_correct(buttonB)

def keypress_C():
    check_correct(buttonC)

def keypress_D():
    check_correct(buttonD)

QnA = QAndA()
# window
window = Tk()
window.title("FRIENDS QUIZ")
window.minsize(700, 500)
window.config(padx=40, pady=40, bg=BEIGE)
# FRIENDS Logo
canvas = Canvas(width=640, height=106, highlightthickness=0, bg=BEIGE)
friends_logo_img = PhotoImage(file="Friends_logo.png")
canvas.create_image(320, 53, image=friends_logo_img)
# timer_text = canvas.create_text(105, 130, text="QUIZ", fill="black", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=0, row=1, columnspan=2)
# Buttons
buttonA = Button(highlightthickness=0, font=(FONT_NAME2, 18), width=20, height=2, command=keypress_A,
                 wraplength=280)
buttonB = Button(highlightthickness=0, font=(FONT_NAME2, 18), width=20, height=2, command=keypress_B,
                 wraplength=280)
buttonC = Button(highlightthickness=0, font=(FONT_NAME2, 18), width=20, height=2, command=keypress_C,
                 wraplength=280)
buttonD = Button(highlightthickness=0, font=(FONT_NAME2, 18), width=20, height=2, command=keypress_D,
                 wraplength=280)
# Question
question_label = Label(text="", font=(FONT_NAME2, 20), bg=BEIGE, fg="black",  wraplength=620, height=5)
question_label.config(padx=10, pady=10)
question_label.grid(column=0, row=2, columnspan=2)
# Start Game Button
start_game_button = Button(text="Press to Start", command=start_game)
start_game_button.config(font=(FONT_NAME, 22, "italic"), bg=BEIGE, fg="black")
start_game_button.grid(column=0, row=2, columnspan=2)
# result_label
result_label = Label(text="", font=(FONT_NAME2, 20), bg=BEIGE, fg="black",  wraplength=620, height=2)
result_label.grid(column=0, row=5, columnspan=2)
# Score Label
score_label = Label(text=f"Score: {score:02d}", font=(FONT_NAME, 20), bg=BEIGE, fg="black", height=2)
score_label.config(padx=20, pady=20)
score_label.grid(column=0, row=0)
# High Score Label
high_sc_label = Label(text=f"High Score: {HIGH_SCORE}", font=(FONT_NAME, 20), bg=BEIGE, fg="black")
high_sc_label.config(padx=20, pady=20)
high_sc_label.grid(column=1, row=0)
# next_question Button
next_question_button = Button(text="Next Question", font=(FONT_NAME, 20), bg=BEIGE, fg="black", command=next_quest)

window.mainloop()
