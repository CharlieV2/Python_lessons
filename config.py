from configparser import *
conf = RawConfigParser()
conf.read('styles.ini')
print(conf.options('Classic'))






#from tkinter import filedialog as fd
#fd.askopenfilename()
