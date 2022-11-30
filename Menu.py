from tkinter import *
import mysql.connector as m
from tkinter import ttk
import SQL_Scoring
root=Tk()
root.geometry("1280x720")
root.title("Main Menu")

#---------------------------------------------------------------------------

def startgame():
    win1 = Tk()
    win1.geometry('800x400')
    win1.grid()
    win1.title("Start Game")
    def back():
        win1.destroy()
    
    def retrieve_input():
        name=textBox.get("1.0","end-1c")
        win1.destroy()
        SQL_Scoring.run_game(name)
    
    Label(win1, text= "Enter name:", font=("Calibri",14)).grid(column=0, row = 0)
    textBox=Text(win1, height=2, width=10)
    textBox.grid(column=1,row = 0)
    buttonCommit=Button(win1, height=1, width=10, text="Enter", command=lambda: retrieve_input())
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit.grid(column=1,row = 1)

    
#---------------------------------------------------------------------------

def rules():
    win4 = Tk()
    win4.geometry("600x500")
    win4.grid()
    win4.title("Rules")
    rule = Label(win4, text= '''Rules\n 
1. Use WASD or arrow keys to move. \n
2. To kill the enemy, overlap with the enemy and press space.\n
3. The player has 100 health. Every bullet does 20 damage.\n
4. The enemy will shoot at the player if the player comes within \n 200 pixels radius and lies in a 120˚ arc. \n
5. The game starts with you and 3 enemies on the screen. \nEvery 5 seconds a new enemy enters. Kill them all to win!\n
''', font=("Calibri",14),border=3).grid()
    def back():
        win4.destroy()
    goback=Button(win4, text= "Back", font=("Calibri",14), command=back, bg="#cdcdcd", fg='black').grid(column=14, row=1)
    
#---------------------------------------------------------------------------

def endgame():
    win2 = Tk()
    win2.geometry("400x200")
    win2.grid()
    win2.title("End Game")
    def end():
        root.destroy()
        win2.destroy()
    def cont():
        win2.destroy()
    label=Label(win2, text= "Are you sure you want to exit?", font=("Calibri",14)).grid(column=0, row=0)
    yes=Button(win2, text= "Yes", font=("Calibri",14), command=end, bg="#cdcdcd", fg='black').grid(column=1, row=1)
    no=Button(win2, text= "No", font=("Calibri",14), command=cont, bg="#cdcdcd", fg='black').grid(column=2, row=1)

#---------------------------------------------------------------------------

def leaderboard():
    win3 = Tk()
    win3.geometry('1000x400')
    win3.grid()
    win3.title("Leaderboard")
    tree = ttk.Treeview(win3,column = ('c1','c2','c3','c4'), show = 'headings')
    tree.column('#1',anchor = CENTER)
    tree.heading('#1', text = 'Rank')
    tree.column('#2',anchor = CENTER)
    tree.heading('#2', text = 'Name')
    tree.column('#3',anchor = CENTER)
    tree.heading('#3', text = 'Score')
    tree.column('#4',anchor = CENTER)
    tree.heading('#4', text = 'Time')
    tree.anchor(CENTER)
    tree.grid(columnspan=5, rowspan= 6)
    con = m.connect(host = 'localhost', username = 'root', passwd = 'fab4', db = 'project')
    mycursor = con.cursor()
    query = 'select * from leaderboard'
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        tree.insert("", END, values = row)
    con.close()
    def back():
        win3.destroy()
    goback=Button(win3, text= "Back", font=("Calibri",14), command=back, bg="#cdcdcd", fg='black').grid(column= 10, row=16)
#---------------------------------------------------------------------------

Startgame = Button(root, text="Start Game", command=startgame, padx= 30 , pady= 30)
Startgame.pack()

Rules = Button(root, text="Rules", command=rules, padx= 30 , pady= 30)
Rules.pack()

Leaderboard = Button(root, text="Leaderboard", command=leaderboard, padx= 30 , pady= 30)
Leaderboard.pack()

Endgame = Button(root, text="End Game", command=endgame, padx= 30 , pady= 30)
Endgame.pack()

root.mainloop()