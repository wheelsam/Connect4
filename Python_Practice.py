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
        global turn_number = 0
        buttons = []

        for x in range(7):
<<<<<<< HEAD
            buttons.append(tk.Button(self, text="Put Piece Here",
                                     command=turn))
            buttons[x].pack(side="left")

    def turn(self):
        turn_number += 1
        if turn_number % 2 == 0:
            print("Player 1 went")
        else:
            print("Player 2 went")
=======
            buttons.append(tk.Button(self, text="Put Piece Here"))
            buttons[x].pack(side="left")

    def player_1(self):
        print("Player 1 went")

    def player_2(self):
        print("Player 2 went")
>>>>>>> a481e4dcae437476a6b89f43fea886c1b1df380d

root = tk.Tk()
root.title("Connect 4")
root.geometry('800x600')
app = Application(master=root)
app.mainloop()
