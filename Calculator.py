from tkinter import *
from tkinter import ttk
root = Tk(); root.title('Calculator'); root.geometry('226x360+300+100'); root.resizable(False,False)
text = ''; znak = ''; memory = []

def ravno():
    global text, znak, memory, answer
    memory.append(enter.get())
    s = 0
    while s != len(memory)-1:
        if s == 0:
            try:
                answer = float(memory[s])
            except ValueError:
                bc(err=2)
        if memory[s+1] == '+':
            try:
                answer += float(memory[s+2])
            except ValueError:
                bc(err=2)
        if memory[s+1] == '-':
            try:
                answer -= float(memory[s+2])
            except ValueError:
                bc(err=2)
        if memory[s+1] == '*':
            try:
                answer *= float(memory[s+2])
            except ValueError:
                bc(err=2)
        try:
            if memory[s+1] == '/':
                try:
                    answer /= float(memory[s+2])
                except ValueError:
                    bc(err=2)
        except ZeroDivisionError:
            bc(err=1)
        s += 2
    if str(answer)[-2:] == '.0':
        answer = int(answer)
    if len(str(answer)) > 13:
        answer = str(answer)[:13]
    enter.delete('0', END)
    enter.insert(INSERT, answer)
    memory = []
    text = str(answer)
def one():
    global text
    text += '1'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def two():
    global text
    text += '2'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def thr():
    global text
    text += '3'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def fou():
    global text
    text += '4'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def fiv():
    global text
    text += '5'
    enter.delete('0', END)
    enter.insert(INSERT, text)   
def six():
    global text
    text += '6'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def sev():
    global text
    text += '7'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def eig():
    global text
    text += '8'
    enter.delete('0', END)
    enter.insert(INSERT, text)  
def nin():
    global text
    text += '9'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def zer():
    global text
    text += '0'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def d0():
    global text
    text += '00'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def plus():
    global text, znak, memory
    if str(enter.get()) != '+' and str(enter.get()) != '-' and str(enter.get()) != '*' and str(enter.get()) != '/':
        memory.append(enter.get())
    if memory[len(memory)-1] == '+' or memory[len(memory)-1] == '-' or memory[len(memory)-1] == '*' or memory[len(memory)-1] == '/':
        del memory[len(memory)-1]
    memory.append('+')
    enter.delete('0', END)
    enter.insert(INSERT, '+')
    text = ''
def minus():
    global text, znak, memory
    if str(enter.get()) != '+' and str(enter.get()) != '-' and str(enter.get()) != '*' and str(enter.get()) != '/':
        memory.append(enter.get())
    if memory[len(memory)-1] == '+' or memory[len(memory)-1] == '-' or memory[len(memory)-1] == '*' or memory[len(memory)-1] == '/':
        del memory[len(memory)-1]
    memory.append('-')
    enter.delete('0', END)
    enter.insert(INSERT, '-')
    text = ''
def umn():
    global text, znak, memory
    if str(enter.get()) != '+' and str(enter.get()) != '-' and str(enter.get()) != '*' and str(enter.get()) != '/':
        memory.append(enter.get())
    if memory[len(memory)-1] == '+' or memory[len(memory)-1] == '-' or memory[len(memory)-1] == '*' or memory[len(memory)-1] == '/':
        del memory[len(memory)-1]
    memory.append('*')
    enter.delete('0', END)
    enter.insert(INSERT, '*')
    text = ''
def delenie():
    global text, znak, memory
    if str(enter.get()) != '+' and str(enter.get()) != '-' and str(enter.get()) != '*' and str(enter.get()) != '/':
        memory.append(enter.get())
    if memory[len(memory)-1] == '+' or memory[len(memory)-1] == '-' or memory[len(memory)-1] == '*' or memory[len(memory)-1] == '/':
        del memory[len(memory)-1]
    memory.append('/')
    enter.delete('0', END)
    enter.insert(INSERT, '/')
    text = ''
def zap():
    global text
    if enter.get() == '+' or enter.get() == '-' or enter.get() == '*' or enter.get() == '/':
        text = '0'
        enter.delete('0', END)
        enter.insert(INSERT, text)
    text = enter.get()
    text += '.'
    enter.delete('0', END)
    enter.insert(INSERT, text)
def bc(err=None):
    global text, znak, memory
    text = ''; znak = ''; memory = []
    if err == 1:
        enter.delete('0', END); enter.insert(INSERT, 'Error: Zero...')
    elif err == 2:
        enter.delete('0', END); enter.insert(INSERT, 'Error: Value...')
    else:
        enter.delete('0', END); enter.insert(INSERT, '0')

fr_enter = Frame(root)
fr_enter.pack()
enter = ttk.Entry(fr_enter, font = 'Arial 22', justify = "right")
enter.pack(ipady = 10, ipadx = 50); enter.insert(INSERT, '0')

fr_but1 = Frame(root)
fr_but1.pack()
but1 = ttk.Button(fr_but1, text = '1', width = 5, command = one, style = "NUM.TButton")
but1.pack(ipady = 7, side = LEFT)

but2 = ttk.Button(fr_but1, text = '2', width = 5, command = two, style = "NUM.TButton")
but2.pack(ipady = 7, side = LEFT)

but3 = ttk.Button(fr_but1, text = '3', width = 5, command = thr, style = "NUM.TButton")
but3.pack(ipady = 7, side = LEFT)

fr_but2 = Frame(root)
fr_but2.pack()
but4 = ttk.Button(fr_but2, text = '4', width = 5, command = fou, style = "NUM.TButton")
but4.pack(ipady = 7, side = LEFT)

but5 = ttk.Button(fr_but2, text = '5', width = 5, command = fiv, style = "NUM.TButton")
but5.pack(ipady = 7, side = LEFT)

but6 = ttk.Button(fr_but2, text = '6', width = 5, command = six, style = "NUM.TButton")
but6.pack(ipady = 7, side = LEFT)

fr_but3 = Frame(root)
fr_but3.pack()
but7 = ttk.Button(fr_but3, text = '7', width = 5, command = sev, style = "NUM.TButton")
but7.pack(ipady = 7, side = LEFT)

but8 = ttk.Button(fr_but3, text = '8', width = 5, command = eig, style = "NUM.TButton")
but8.pack(ipady = 7, side = LEFT)

but9 = ttk.Button(fr_but3, text = '9', width = 5, command = nin, style = "NUM.TButton")
but9.pack(ipady = 7, side = LEFT)

fr_but4 = Frame(root)
fr_but4.pack()
butp = ttk.Button(fr_but4, text = '+', width = 5, command = plus, style = "MOV.TButton")
butp.pack(ipady = 7, side = LEFT)

but0 = ttk.Button(fr_but4, text = '0', width = 5, command = zer, style = "NUM.TButton")
but0.pack(ipady = 7, side = LEFT)

butu = ttk.Button(fr_but4, text = '*', width = 5, command = umn, style = "MOV.TButton")
butu.pack(ipady = 7, side = LEFT)

fr_but5 = Frame(root)
fr_but5.pack()
butm = ttk.Button(fr_but5, text = '-', width = 5, command = minus, style = "MOV.TButton")
butm.pack(ipady = 7, side = LEFT)

butr = ttk.Button(fr_but5, text = '=', width = 5, command = ravno, style = "MOV.TButton")
butr.pack(ipady = 7, side = LEFT)

butd = ttk.Button(fr_but5, text = '/', width = 5, command = delenie, style = "MOV.TButton")
butd.pack(ipady = 7, side = LEFT)

fr_but6 = Frame(root)
fr_but6.pack()

butc = ttk.Button(fr_but6, text = 'C', width = 5, command = bc, style = "MOV.TButton")
butc.pack(ipady = 7, side = LEFT)

butz = ttk.Button(fr_but6, text = ',', width = 5, command = zap, style = "NUM.TButton")
butz.pack(ipady = 7, side = LEFT)

but00 = ttk.Button(fr_but6, text = '00', width = 5, command = d0, style = "NUM.TButton")
but00.pack(ipady = 7, side = LEFT)


style = ttk.Style(root)
style.configure('TButton', font = 'Arial 17', padding=1, background="#ccc")
style.map("NUM.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])
style.map("MOV.TButton", foreground=[('pressed', 'white'), ('active', 'red')])
root.mainloop()






