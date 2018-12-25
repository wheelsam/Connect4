from tkinter import *
import tkinter as tk
turn_number = 1
board_layout = [[]]
x=0
cs=0
board_layout=[[x,x,x,x,x,x,x],[x,x,x,x,x,x,x],[x,x,x,x,x,x,x],[x,x,x,x,x,x,x],[x,x,x,x,x,x,x],[x,x,x,x,x,x,x]]
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()

    def create_board(self):
        self.create_buttons()
        grid_layout=[]



        Lbl = Label(self, bg="Green",text ="C4 demo")
        Lbl.grid(row=1,column=3)

        rows = 7
        for i in range(1,rows):
            for j in range(7):
                grid_layout = Label(self, text="""

                            """, bg="Gray",relief="groove")
                grid_layout.grid(row=i+2, column=j)

    def create_buttons(self):
        buttons = []

        Lbl2 = Label(self,text = "\nPlace a piece\n(use the buttons)")
        Lbl2.grid(row=10,column=3)
        Lbl3 = Label(self, text = "Player 1\ Go")
        Lbl3.grid(row=15,column=3)
        #Keeps track of whos turn it is and does stuff
        def turn():
            global turn_number
            turn_number += 1

            if turn_number % 2 == 0:
                Lbl3 = Label(self,text = "Player 1\n\ Go")
                Lbl3.grid(row=15,column=3)
                def edit_col1():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][0]==0:
                            board_layout [x][0]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col2():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][1]==0:
                            board_layout [x][1]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col3():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][2]==0:
                            board_layout [x][2]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col4():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][3]==0:
                            board_layout [x][3]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col5():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][4]==0:
                            board_layout [x][4]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col6():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][5]==0:
                            board_layout [x][5]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col7():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][6]==0:
                            board_layout [x][6]=1
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1

                B1 = Button(self, text = "Col1", command = edit_col1)
                B1.grid(row=9,column = 0)
                B2 = Button(self, text = "Col2", command = edit_col2)
                B2.grid(row=9,column = 1)
                B3 = Button(self, text = "Col3", command = edit_col3)
                B3.grid(row=9,column = 2)
                B4 = Button(self, text = "Col4", command = edit_col4)
                B4.grid(row=9,column = 3)
                B5 = Button(self, text = "Col5", command = edit_col5)
                B5.grid(row=9,column = 4)
                B6 = Button(self, text = "Col6", command = edit_col6)
                B6.grid(row=9,column = 5)
                B7 = Button(self, text = "Col7", command = edit_col7)
                B7.grid(row=9,column = 6)
            else:
                Lbl3 = Label(self,text = "Player 2\n Go")
                Lbl3.grid(row=15,column=3)
                def edit_col1():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][0]==0:
                            board_layout [x][0]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col2():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][1]==0:
                            board_layout [x][1]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col3():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][2]==0:
                            board_layout [x][2]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col4():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][3]==0:
                            board_layout [x][3]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col5():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][4]==0:
                            board_layout [x][4]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col6():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][5]==0:
                            board_layout [x][5]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                def edit_col7():
                    cs=0
                    x=0
                    while cs==0:
                        if board_layout[x][6]==0:
                            board_layout [x][6]=2
                            print(str(board_layout[0])+ "\n" + str(board_layout[1])+"\n" +str(board_layout[2])+ "\n" +str(board_layout[3])+ "\n" +str(board_layout[4])+ "\n" +str(board_layout[5]))
                            cs=1
                        else:
                            x+=1
                B1 = Button(self, text = "Col1", command = edit_col1)
                B1.grid(row=9,column = 0)
                B2 = Button(self, text = "Col2", command = edit_col2)
                B2.grid(row=9,column = 1)
                B3 = Button(self, text = "Col3", command = edit_col3)
                B3.grid(row=9,column = 2)
                B4 = Button(self, text = "Col4", command = edit_col4)
                B4.grid(row=9,column = 3)
                B5 = Button(self, text = "Col5", command = edit_col5)
                B5.grid(row=9,column = 4)
                B6 = Button(self, text = "Col6", command = edit_col6)
                B6.grid(row=9,column = 5)
                B7 = Button(self, text = "Col7", command = edit_col7)
                B7.grid(row=9,column = 6)




            def isGameWon():
                print(board_layout)

            isGameWon()

        #Creates a row of 7 buttons that do the turn method when clicked
        for x in range(1):

            buttons.append(tk.Button(self, text=" Confirm %d " %1,
                                     command=turn))
            buttons[x].grid(row=12,column=x)










#Global variables

#Keeps track of where pieces are, 0 means none, 1 means player 1
#and 2 means player 2




root = tk.Tk()
root.title("Connect 4")
root.geometry('1000x600')
app = Application(master=root)
app.mainloop()
