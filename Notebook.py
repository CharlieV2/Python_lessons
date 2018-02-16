import tkinter
from tkinter import ttk
root = tkinter.Tk()
n = ttk.Notebook(root)
n.pack(fill='both', expand=True)
pages = []
for page in range(5):
    child = ttk.Frame(root)
    lab = ttk.Label(child, text='text %i'%page)
    lab.pack()
    n.add(child, text ='page %i'%page )
    pages.append(child)
    
textForPage1 = tkinter.Text(pages[1])
textForPage1.pack(fill='both', expand=True)
root.mainloop()