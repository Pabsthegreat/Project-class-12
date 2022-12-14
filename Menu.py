from tkinter import *
import mysql.connector as m
from tkinter import ttk
import SQL_Scoring
root=Tk()
root.geometry("800x600")
root.title("Main Menu")
root.configure(background = '#000000')
Label(root, text = "Hunter Assassin", font = ('Comic Sans MS', 48), bg = '#000000', fg = '#ffffff').pack(anchor=CENTER)
#---------------------------------------------------------------------------

def startgame():
    win1 = Tk()
    win1.geometry('400x400')
    win1.grid()
    win1.title("Start Game")
    win1.configure(bg = '#ff636f')
    
    def win():
        winn = Tk()
        winn.geometry('300x300')
        winn.grid()
        winn.title("Victory!")
        winn.configure(bg = '#ff636f')
        
        Label(winn, text = 'Congratulations!!! \nYou win!🥳🥳🥳', font = ("Comic Sans MS", 14), border = 3, bg = '#ff636f').place(x = 50, y = 50)
        Button(winn, text = "Back", font = ("Comic Sans MS", 14), command = winn.destroy).place(x = 200, y = 200)

    def lose():
        lose = Tk()
        lose.geometry('300x300')
        lose.grid()
        lose.title("Defeat")
        lose.configure(bg = '#ff636f')
        
        Label(lose, text = 'You Lose 😕 \nBetter Luck Next Time.', font = ("Comic Sans MS", 14), border = 3, bg = '#ff636f').place(x = 50, y = 50)
        Button(lose, text = "Back", font = ("Comic Sans MS", 14), command = lose.destroy).place(x = 200, y = 200)

    def retrieve_input():
        name = textBox.get("1.0", "end-1c")
        win1.destroy()
        result = SQL_Scoring.run_game(name)
        
        if result == 'win':
            win()
        elif result == 'lose':
            lose()

    Label(win1, text = "Enter name:", font = ('Comic Sans MS', 16), bg = '#ff636f').place(x = 70, y = 150)
    textBox = Text(win1, height = 1, width = 10, font = ('Comic Sans MS',12))
    textBox.place(x = 200, y = 155)
    buttonCommit = Button(win1, height = 1, width = 10, text = "Enter", font = ('Comic Sans MS', 12), command = lambda:retrieve_input())
    #command = lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit.place(x = 150, y = 200)
    Button(win1, text = "Back", font = ("Comic Sans MS", 14), command = win1.destroy).place(x = 300, y = 300)

    
#---------------------------------------------------------------------------

def rules():
    win4 = Tk()
    win4.geometry("600x500")
    win4.grid()
    win4.title("Rules")
    win4.configure(bg = '#ff636f')

    Label(win4, text = '''Rules\n 
1. Use WASD or arrow keys to move. \n
2. To kill the enemy, overlap with the enemy and press space.\n
3. The player has 100 health. Every bullet does 25 damage.\n
4. The enemy will shoot at the player if the player comes within \n 200 pixels radius and lies in a 120˚ arc. \n
5. The game starts with you and 3 enemies on the screen. \nEvery 5 seconds a new enemy enters. Kill them all to win!\n''',
font = ("Comic Sans MS", 14), border = 3, bg = '#ff636f').pack(anchor = CENTER)

    Button(win4, text = "Back", font = ("Comic Sans MS", 14), command = win4.destroy).place(x = 500, y = 400)
    
#---------------------------------------------------------------------------

def endgame():
    win2 = Tk()
    win2.geometry("400x200")
    win2.grid()
    win2.title("End Game")
    win2.configure(bg = '#ff636f')
    
    def end():
        win2.destroy()
        root.destroy()
    
    Label(win2, text = "Are you sure you want to exit?", font = ("Comic Sans MS", 18), bg = '#ff636f').place(x = 20, y = 30)
    Button(win2, text = "Yes", font = ("Comic Sans MS", 14), command = end, border = 3).place(x = 250, y = 100)
    Button(win2, text = "No", font = ("Comic Sans MS", 14), command = win2.destroy, border = 3).place(x = 300, y = 100)

#---------------------------------------------------------------------------

def leaderboard():
    win3 = Tk()
    win3.geometry('1000x400')
    win3.grid()
    win3.title("Leaderboard")
    win3.configure(bg = '#ff636f')

    tree = ttk.Treeview(win3, column = ('c1','c2','c3','c4'), show = 'headings', height = 10)
    
    tree.column('#1', anchor = CENTER)
    tree.heading('#1', text = 'Rank')

    tree.column('#2', anchor = CENTER)
    tree.heading('#2', text = 'Name')
    
    tree.column('#3', anchor = CENTER)
    tree.heading('#3', text = 'Score')
    
    tree.column('#4', anchor = CENTER)
    tree.heading('#4', text = 'Time')
    
    tree.pack()
    con = m.connect(host = 'localhost', username = 'root', passwd = 'fab4', db = 'project')
    mycursor = con.cursor()
    query = 'select * from leaderboard'
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        tree.insert("", END, values = row)
        pass
    con.close()
    
    Button(win3, text = "Back", font = ('Comic Sans MS', 16), command = win3.destroy).place(x = 900, y = 300)
#---------------------------------------------------------------------------

Startgame = Button(root, text = "Start Game", font = ('Comic Sans MS', 16), command = startgame, padx = 20 , pady = 20, bg = '#c0ae39', fg = '#000000')
Startgame.pack()

Rules = Button(root, text = "Rules", font = ('Comic Sans MS', 16), command = rules, padx = 20 , pady = 20, bg = '#c0ae39', fg = '#000000')
Rules.pack()

Leaderboard = Button(root, text = "Leaderboard", font = ('Comic Sans MS', 16), command = leaderboard, padx = 20 , pady = 20, bg = '#c0ae39', fg = '#000000')
Leaderboard.pack()

Endgame = Button(root, text = "End Game", font = ('Comic Sans MS', 16), command = endgame, padx = 20 , pady = 20, bg = '#c0ae39', fg = '#000000')
Endgame.pack()

root.mainloop()