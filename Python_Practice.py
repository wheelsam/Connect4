from tkinter import *

board_layout = [[0 for x in range(7)]for y in range(6)]
turn_number = 1

class Application(Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()

    def create_board(self):
        self.create_buttons()
        grid_layout = []



        Lbl = Label(self, bg = "Green", text = "C4 demo")
        Lbl.grid(row = 1, column = 3)

        for i in range(1,7):
            for j in range(7):
                grid_layout = Label(self, text = """

                            """, bg="Gray",relief="groove")
                grid_layout.grid(row = i + 2, column = j)

    def create_buttons(self):
        buttons = []
        player_text = StringVar()
        player_turn = Label(self, textvariable = player_text)
        player_text.set("Player 1\n Go")
        player_turn.grid(row = 15, column = 3)

        for x in range(7):
            buttons.append(Button(self, text = "Go Here", command = lambda
                                  column = x: self.turn(column, player_text)))
            buttons[x].grid(row = 9, column = x)

    #Keeps track of whos turn it is. Puts a number in a column depending on which button is pressed
    def turn(self, column, player_text):
        global board_layout
        global turn_number
        turn_number += 1
        cs = 0
        r = 0

        while cs == 0:
            if board_layout[r][column] == 0:
                board_layout [r][column] = turn_number % 2 + 1
                for y in range(6):
                    print(str(board_layout[y]) + "\n")
                cs = 1
            else:
                if r == 5:
                    turn_number += 1
                    return
                r += 1

        if turn_number % 2 == 1:
            player_text.set("Player 1\n Go")
        else:
            player_text.set("Player 2\n Go")

        def isGameWon():
            print(1)

        isGameWon()


root = Tk()
root.title("Connect 4")
root.geometry('1000x600')
app = Application(master=root)
app.mainloop()
