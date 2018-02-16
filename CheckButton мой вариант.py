from tkinter import *
root = Tk()
n = 1
def check():
    global n
    if n == 0:
        n = 1
    elif n == 1:
        n = 0
g = Checkbutton(root, command = check); g.pack()
g.select()
def v():
    global n
    print(n)
Button(root, text = 'check', command = v).pack()

root.mainloop()