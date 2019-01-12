from tkinter import *

board_layout = [[0 for x in range(7)]for y in range(6)]
turn_number = 1
SQUARE_SIZE = 10

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
                grid_layout = Label(self, height = 4, width = 12, bg="Gray",relief="groove")
                grid_layout.grid(row = i + 2, column = j)


    def create_buttons(self):
        buttons = []
        #Making the changing player turn
        player_text = StringVar()
        player_text.set("Player 1\n Go")
        player_turn = Label(self, textvariable = player_text)
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
        piece = turn_number % 2 + 1
        cs = 0
        r = 5

        while cs == 0:
            if board_layout[r][column] == 0:
                if piece == 1:
                    grid_layout = Label(self, height = 4, width = 12, bg="Blue",relief="groove")
                else:
                    grid_layout = Label(self, height = 4, width = 12, bg="Red",relief="groove")
                board_layout [r][column] = piece
                grid_layout.grid(row = r + 2, column = column)
                cs = 1
            else:
                if r == 0:
                    turn_number += 1
                    return
                r -= 1

        #Bad because it creates an array of 42 buttons each time a button is pressed
        #self.create_board()
        if piece - 1 == 1:
            player_text.set("Player 1\n Go")
        else:
            player_text.set("Player 2\n Go")

        if self.checkVertandHor(r, column, piece) or self.checkDiagonalBackwards(r, column, piece) or self.checkDiagonalForward(r, column, piece):
            self.gameWon(piece)

    def gameWon(self, piece):
        print("Player %d wins!" % piece)

    def checkDiagonalForward(self, r, column, piece):
        while (r < 5 and column > 0):
            r += 1
            column -= 1
        counter = 0
        while (r >= 0 and column <= 6):
            if board_layout[r][column] == piece:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
            r -= 1
            column += 1
        return False

    def checkDiagonalBackwards(self, r, column, piece):
        while (r > 0 and column > 0):
            r -= 1
            column -= 1
        counter = 0
        while (r <= 5 and column <= 6):
            if board_layout[r][column] == piece:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
            r += 1
            column += 1
        return False

    def checkVertandHor(self, r, column, piece):
        counter = 0
        for x in range(6):
            if board_layout[x][column] == piece:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
        counter = 0
        for y in range(7):
            if board_layout[r][y] == piece:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
        return False



root = Tk()
root.title("Connect 4")
root.geometry('1000x600')
app = Application(master=root)
app.mainloop()
