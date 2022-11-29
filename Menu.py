from tkinter import *
import mysql.connector as m
from tkinter import ttk
import SQL_Scoring
root=Tk()
root.geometry("800x600")
root.title("Main Menu")
root.configure(background = '#000000')
Label(root,text = "Hunter Assassin", font = ('Comic Sans MS',48), bg='#000000',fg='#ffffff').pack(anchor=CENTER)
#---------------------------------------------------------------------------

def startgame():
    win1 = Tk()
    win1.geometry('400x400')
    win1.grid()
    win1.title("Start Game")
    win1.configure(bg = '#ff636f')
    def back():
        win1.destroy()
    
    def retrieve_input():
        name=textBox.get("1.0","end-1c")
        win1.destroy()
        SQL_Scoring.run_game(name)
    
    Label(win1, text= "Enter name:", font = ('Comic Sans MS',16),bg = '#ff636f').place(x = 70, y = 150)
    textBox=Text(win1, height=2, width=10)
    textBox.place(x = 200, y = 150)
    buttonCommit=Button(win1, height=1, width=10, text="Enter",font=('Comic Sans MS',12), command=lambda: retrieve_input())
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit.place( x= 150, y = 200)

    
#---------------------------------------------------------------------------

def rules():
    win4 = Tk()
    win4.geometry("600x500")
    win4.grid()
    win4.title("Rules")
    win4.configure(bg = '#ff636f')
    Label(win4, text= '''Rules\n 
1. Use WASD or arrow keys to move. \n
2. To kill the enemy, overlap with the enemy and press space.\n
3. The player has 100 health. Every bullet does 20 damage.\n
4. The enemy will shoot at the player if the player comes within \n 200 pixels radius and lies in a 120˚ arc. \n
5. The game starts with you and 3 enemies on the screen. \nEvery 5 seconds a new enemy enters. Kill them all to win!\n
''', font=("Comic Sans MS",14),border=3,bg = '#ff636f').pack(anchor = CENTER)
    def back():
        win4.destroy()
    goback=Button(win4, text= "Back", font=("Comic Sans MS",14), command=back).place(x= 500,y=400)
    
#---------------------------------------------------------------------------

def endgame():
    win2 = Tk()
    win2.geometry("400x200")
    win2.grid()
    win2.title("End Game")
    win2.configure(bg = '#ff636f')
    def end():
        root.destroy()
        win2.destroy()
    def cont():
        win2.destroy()
    label=Label(win2, text= "Are you sure you want to exit?", font=("Comic Sans MS",18),bg = '#ff636f').place(x =20, y = 30)
    yes=Button(win2, text= "Yes", font=("Comic Sans MS",14), command=end,border= 3).place(x =250, y = 100)
    no=Button(win2, text= "No", font=("Comic Sans MS",14), command=cont,border= 3).place(x =300, y = 100)

#---------------------------------------------------------------------------

def leaderboard():
    win3 = Tk()
    win3.geometry('1000x400')
    win3.grid()
    win3.title("Leaderboard")
    win3.configure(bg = '#ff636f')
    tree = ttk.Treeview(win3,column = ('c1','c2','c3','c4'), show = 'headings')
    tree.column('#1',anchor = CENTER)
    tree.heading('#1', text = 'Rank')
    tree.column('#2',anchor = CENTER)
    tree.heading('#2', text = 'Name')
    tree.column('#3',anchor = CENTER)
    tree.heading('#3', text = 'Score')
    tree.column('#4',anchor = CENTER)
    tree.heading('#4', text = 'Time')
    tree.grid(columnspan=5, rowspan= 6)
    con = m.connect(host = 'localhost', username = 'root', passwd = 'fab4', db = 'project')
    mycursor = con.cursor()
    query = 'select * from leaderboard order by score desc, time asc'
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        tree.insert("", END, values = row)
    con.close()
    def back():
        win3.destroy()
    Button(win3, text= "Back", font=('Comic Sans MS',16), command=back).place(x = 900, y = 300)
#---------------------------------------------------------------------------

Startgame = Button(root, text="Start Game", font = ('Comic Sans MS',16), command=startgame, padx= 20 , pady= 20,bg = '#c0ae39',fg='#000000')
Startgame.pack()

Rules = Button(root, text="Rules",font = ('Comic Sans MS',16), command=rules, padx= 20 , pady= 20,bg = '#c0ae39',fg='#000000')
Rules.pack()

Leaderboard = Button(root, text="Leaderboard",font = ('Comic Sans MS',16), command=leaderboard, padx= 20 , pady= 20,bg = '#c0ae39',fg='#000000')
Leaderboard.pack()

Endgame = Button(root, text="End Game", font = ('Comic Sans MS',16),command=endgame, padx= 20 , pady= 20,bg = '#c0ae39',fg='#000000')
Endgame.pack()

root.mainloop()