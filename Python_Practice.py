from tkinter import *
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()

    def create_board(self):
        self.create_buttons()
        grid_layout=[]



        Lbl = Label(self, text ="C4 demo")
        Lbl.grid(row=1,column=3)

        rows = 7
        for i in range(1,rows):
            for j in range(7):
                grid_layout = Button(self, text="""

                        """)
                grid_layout.grid(row=i+2, column=j)
    def create_buttons(self):
        buttons = []

        #Keeps track of whos turn it is and does stuff
        def turn():
            global turn_number
            turn_number += 1
            if turn_number % 2 == 0:
                print("Player 1 went")
            else:
                print("Player 2 went")
            isGameWon()

        #Creates a row of 7 buttons that do the turn method when clicked
        for x in range(7):
            buttons.append(tk.Button(self, text="Put Piece Here",
                                     command=turn))
            buttons[x].grid(row=9,column=x)

    def isGameWon():

#Global variables

#Keeps track of where pieces are, 0 means none, 1 means player 1
#and 2 means player 2
    #board_layout = [][]
    ###for x in range(7):
        ###buttons.append()
###

            turn_number = 0

root = tk.Tk()
root.title("Connect 4")
root.geometry('800x600')



app = Application(master=root)
app.mainloop()
