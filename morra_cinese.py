from tkinter import *
import random

win = Tk()
win.geometry("750x450")
win.title("Morra Cinese")

computer_options = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

player_score = 0
computer_score = 0

def isrock():
    global player_score, computer_score
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = "Player Wins"
        player_score += 1
    else:
        match_result = "Computer Wins"
        computer_score += 1
    end_match(match_result)

def ispaper():
    global player_score, computer_score
    value = computer_options[str(random.randint(0, 2))]
    if value == "Paper":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = "Computer Wins"
        computer_score += 1
    else:
        match_result = "Player Wins"
        player_score += 1
    end_match(match_result)

def isscissor():
    global player_score, computer_score
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Computer Wins"
        computer_score += 1
    elif value == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Wins"
        player_score += 1
    end_match(match_result)

def end_match(match_result):
    global player_score, computer_score
    if player_score >= 5 or computer_score >= 5:
        label_result.config(text="Game Over! Final Score: Player " + str(player_score) + " - " + "Computer " + str(computer_score))
        button_rock.config(state="disabled")
        button_paper.config(state="disabled")
        button_scissor.config(state="disabled")
    else:
        label_result.config(text=match_result)
    label_player_score.config(text="Player: " + str(player_score))
    label_computer_score.config(text="Computer: " + str(computer_score))

label_title = Label(win, text="Rock Paper Scissor", font="normal 20 bold", fg="grey")
label_title.pack(pady=20)

frame_buttons = Frame(win)
frame_buttons.pack(pady=20)

button_rock = Button(frame_buttons, text="Rock", width=10, height=2, command=isrock)
button_paper = Button(frame_buttons, text="Paper", width=10, height=2, command=ispaper)
button_scissor = Button(frame_buttons, text="Scissor", width=10, height=2, command=isscissor)

button_rock.pack(side=LEFT, padx=20)
button_paper.pack(side=LEFT, padx=20)
button_scissor.pack(side=LEFT, padx=20)

label_score = Label(win, text="Score", font="normal 16 bold")
label_score.pack()

label_player_score = Label(win, text="Player: " + str(player_score), font="normal 14")
label_player_score.pack()

label_computer_score = Label(win, text="Computer: " + str(computer_score), font="normal 14")
label_computer_score.pack()

label_result = Label(win, text="", font="normal 20 bold", fg="blue")
label_result.pack(pady=20)

win.mainloop()