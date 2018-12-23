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
        global turn_number
        turn_number = 0
        buttons = []


        def turn():
            turn_number += 1
            if turn_number % 2 == 0:
                print("Player 1 went")
            else:
                print("Player 2 went")

        for x in range(7):
            buttons.append(tk.Button(self, text="Put Piece Here",
                                     command=turn))
            buttons[x].pack(side="left")


root = tk.Tk()
root.title("Connect 4")
root.geometry('800x600')
app = Application(master=root)
app.mainloop()
