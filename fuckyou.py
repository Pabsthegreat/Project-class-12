import tkinter
#from tkinter import ttk

def win1():
    win = tkinter.Tk()
    win.geometry("360x120")
    win.grid()

    #win.title("Click the Button to Close the Window")
    def close():
        win2 = tkinter.Tk()
        win2.geometry("350x120")
        win2.grid()
        win2.quit()
        def end():
            win.destroy()
            win2.destroy()
        def cont():
            win2.destroy()            
           
        label= tkinter.Label(win2, text= "Are you sure you want to exit?", font=("Calibri",14)).grid(column=0, row=0)
        yes= tkinter.Button(win2, text= "Yes", font=("Calibri",14), command=end, bg="#cdcdcd", fg='black').grid(column=1, row=1)
        no = tkinter.Button(win2, text= "No", font=("Calibri",14), command=cont, bg="#cdcdcd", fg='black').grid(column=2, row=1)

    exit1= tkinter.Button(win, text= "Exit Application", font=("Calibri",14), command=close, bg="#a52a2a", fg='white').grid(column=0, row=1)

    win.mainloop()

win1()