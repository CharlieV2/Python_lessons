from tkinter import Tk, Toplevel, Button
def openModal():
    modal_win = Toplevel(root)
    modal_win.grab_set()
    modal_win.focus_set()
    modal_win.wait_window()
root = Tk()
Button(root, text = 'openModal', command = openModal).pack()
root.mainloop()