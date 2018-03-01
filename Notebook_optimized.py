import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('Notebook')
root.geometry('600x400')
root.resizable(0,0)

# # # # # # # # # #

# the tab bar takes 25 pixels from the top
n = ttk.Notebook(root)
n.pack(fill='both', expand = True)

pages = [] # parents for widgets
names = ['page0', 'page1', 'page2'] # page names in order

for page in names:
    child = ttk.Frame(root)
    n.add(child, text = page)
    pages.append(child)

# # # # # # # # # #

# widgets
textForPage0 = tkinter.Text(pages[0])
textForPage0.pack(fill='both', expand=True)

entryForPage1 = tkinter.ttk.Entry(pages[1], font = ('Arial', 13))
entryForPage1.place(x = 5, y = 5, width = 250)

butForPage2 = tkinter.ttk.Button(pages[2], text = 'but1')
butForPage2.place(x = 492, y = 345, w = 100, h = 25)

butForPage2_ = tkinter.ttk.Button(pages[2], text = 'but0')
butForPage2_.place(x = 387, y = 345, w = 100, h = 25)


root.mainloop()