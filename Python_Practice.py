import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()

    def create_board(self):
        self.create_buttons()

    def create_buttons(self):
        buttons = []



        #Creates a row of 7 buttons that do the turn method when clicked
        for x in range(7):
            buttons.append(tk.Button(self, text="Put Piece Here",
                                     command=self.turn))
            buttons[x].pack(side="left")

    #Keeps track of whos turn it is and does stuff
    def turn():
        global turn_number
        turn_number += 1
        if turn_number % 2 == 0:
            print("Player 1 went")
        else:
            print("Player 2 went")
        self.isGameWon()

    def isGameWon():
        return false

#Global variables

#Keeps track of where pieces are, 0 means none, 1 means player 1
#and 2 means player 2
board_layout = [[0 for x in range(7)] for y in range(6)]
print(board_layout)

turn_number = 0

root = tk.Tk()
root.title("Connect 4")
root.geometry('800x600')
app = Application(master=root)
app.mainloop()
