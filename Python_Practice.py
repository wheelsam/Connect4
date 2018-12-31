from tkinter import *

board_layout = [[0 for x in range(7)]for y in range(6)]
turn_number = 1

class Application(Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()
        self.create_buttons()

    def create_board(self):
        grid_layout = []

        Lbl = Label(self, bg = "White", text = "\n Connect Four \n")
        Lbl.grid(row = 1, column = 3)

        for i in range(6):
            for j in range(7):
                if board_layout[i][j] == 0:
                    grid_layout = Label(self, text = "\t\t\n\n\n", bg="Gray",relief="groove")
                if board_layout[i][j] == 1:
                    grid_layout = Label(self, text = "\t\t\n\n\n", bg="Blue",relief="groove")
                if board_layout[i][j] == 2:
                    grid_layout = Label(self, text = "\t\t\n\n\n", bg="Red",relief="groove")
                grid_layout.grid(row = i + 2, column = j)

        #Making the changing player turn
        player_text = StringVar()
        player_turn = Label(self, textvariable = player_text)
        if turn_number % 2 == 1:
            player_text.set("Player 1\n Go")
        else:
            player_text.set("Player 2\n Go")
        player_turn.grid(row = 15, column = 3)


    def create_buttons(self):
        buttons = []

        for x in range(7):
            buttons.append(Button(self, text = "Go Here", command = lambda
                                  column = x: self.turn(column)))
            buttons[x].grid(row = 9, column = x)

    #Keeps track of whos turn it is. Puts a number in a column depending on which button is pressed
    def turn(self, column):
        global board_layout
        global turn_number
        turn_number += 1
        cs = 0
        r = 5

        while cs == 0:
            if board_layout[r][column] == 0:
                board_layout [r][column] = turn_number % 2 + 1
                #for y in range(6):
                #    print(str(board_layout[y]) + "\n")
                cs = 1
            else:
                if r == 0:
                    turn_number += 1
                    return
                r -= 1

        #Bad because it creates an array of 42 buttons each time a button is pressed
        self.create_board()

        self.isGameWon()

    def isGameWon(self):
        x = 1


root = Tk()
root.title("Connect 4")
root.geometry('1000x600')
app = Application(master=root)
app.mainloop()
