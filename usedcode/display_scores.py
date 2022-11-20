from tkinter import *
from scoring import lst
def d_table():

    rows = []

    for i in range (len(lst)):
        columns = []
        for j in range(4):
            e = Entry(relief = GROOVE, font = 'Georgia', justify='center')

            e.grid(row=i, column=j)

            e.insert(END, lst[i][j])

            columns.append(e)

        rows.append(columns)

    mainloop()