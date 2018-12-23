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
<<<<<<< HEAD
            buttons.append(tk.Button(self, text="Put Piece Here"))
            buttons[x].pack(side="left")
=======
            buttons.append(tk.Button(self))

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
>>>>>>> 056a56d1640e68494a53935b4ba1177e80ee8ed2

    def player_1(self):
        print("Player 1 went")

    def player_2(self):
        print("Player 2 went")

root = tk.Tk()
root.title("Connect 4")
root.geometry('350x200')
app = Application(master=root)
app.mainloop()
