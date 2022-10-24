from tkinter import *
import os

root=Tk()
root.geometry("1280x720")

#---------------------------------------------------------------------------

def startgame():
    os.system('yuck.py')

#---------------------------------------------------------------------------

def endgame():
    win2 = Tk()
    win2.geometry("350x120")
    win2.grid()
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
    win3.geometry("1280x720")
    import mysql.connector as m
    obj=m.connect(host="localhost", user="root", passwd="root")
    print(obj.is_connected())
    cur=obj.cursor()
    cur.execute("Show databases")
    databases=cur.fetchall()
    if ('satvik', ) not in databases:
        (cur.execute("create database satvik"))
    cur.execute("use satvik")
    cur.execute("drop table if exists student")

    cur.execute("select * from leaderboard")
    leaderboard=cur.fetchall()
    if not leaderboard:
        label1 = Label(win3, text="Leaderboard is empty.").pack()
    else:
        print("hi")

    obj.commit()

#---------------------------------------------------------------------------

Startgame = Button(root, text="Start Game", command=startgame, padx="50", pady="50")
Startgame.pack()

Endgame = Button(root, text="End Game", command=endgame, padx="50", pady="50")
Endgame.pack()

Leaderboard = Button(root, text="Leaderboard", command=leaderboard, padx="50", pady="50")
Leaderboard.pack()

root.mainloop()