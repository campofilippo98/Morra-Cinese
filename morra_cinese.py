from tkinter import *
from tkinter import ttk
import random

win= Tk()

win.geometry("750x450")

win.title("Morra Cinese")

computer_options = {
   "0":"Rock",
   "1":"Paper",
   "2":"Scissor"
}
def isrock():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Wohoo! You Won"
   else:
      match_result = "Computer Win"

def ispaper():
   value = computer_options[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Computer Win"
   else:
      match_result = "Player Wins"

def isscissor():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Computer Wins"
   elif value == "Scissor":
      match_result = "Match Draw"
   else:
      match_result = "Player Wins"
