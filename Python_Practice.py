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

        for x in range(7):
            buttons.append(tk.Button(self, text="Put Piece Here"))

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def player_1(self):
        print("Player 1 went")

    def player_2(self):
        print("Player 2 went")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
