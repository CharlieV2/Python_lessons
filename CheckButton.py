import tkinter as tk

class gg:
    def __init__(self):
        global g
        g = StringVar()
        self.g = g
    def menu(self, event):
        ro = Toplevel()
        ch = Checkbutton(ro, text='eXample', variable=self.g, onvalue='y', offvalue='n')
        ch.grid(row=0, column=0)
        ch.select()
        b = Button(ro, text='Save', width=8)
        b.bind('<Button-1>', start.pr)
        b.grid(row=1, column=0)

    def pr(self, event):
        print(g.get())
root = Tk()
start = gg()
bs = Button(root, width=10, text='connect')
bs.grid(row=0, column=0)
bs.bind('<Button-1>', start.menu)
root.mainloop()