from tkinter import *
from tkinter import ttk
from clipboard import *
import pyperclip
from tkinter.filedialog import askopenfilename
import base64
win = Tk()
f = ''
win.title('Base 64')
address1 = StringVar()
textbox = Entry(win,textvariable = address1,width = 50,font = 'tahoma 14')
textbox.pack()
def Browseropen():
    global address1
    address1.set(askopenfilename(file = (('Pictures file' , '*.png'),('Pictures file' , '*.jpg'),('Pictures file' , '*.jpeg'))))
Button(win,text = 'Browser',bg = 'black',padx = 54,fg = 'white',command = Browseropen).pack()
text = Text(win)
text.pack()
def convert():
    global address1,f
    with open(address1.get(), "rb") as img_file:
        s = base64.a85encode(img_file.read()).decode('utf-8')
        f = base64.a85decode(s)
        text.insert(END,f'{base64.a85decode(s)}')
def about():
    win2 = Toplevel()
    win2.title("About")
    win2.resizable(False,False)
    ttk.Label(win2,text = 'name app : Picture2Base64\nversion : 1.0\nProduct : HAMMER GROUP\nDevelooper : MOEIN ERSHADI\nCreated App In 28 Line\nPython 3.8 Tkinter\nPicture2base64 2.0 In April 2020\n\n        Hammer & ATTRIB\n\n\nNumber Phone : 02166385045\n\n          Copy Right 2020\n',font = 'tahoma 15').pack()
    exits= Button(win2,text = 'EXIT',bg = 'black',fg = 'white',padx = 54,command = win2.destroy).pack()
def copy():
    global f
    pyperclip.copy(f)
Button(win,text = 'Convert',bg = 'black',fg = 'white',padx = 54,command = convert).pack()
Button(win,text = 'Exit',bg = 'black',padx = 54,fg = 'white',command = win.destroy).pack(side = 'left')
Button(win,text = 'About',bg = 'black',padx = 54,fg = 'white',command = about).pack(side = 'right')
Button(win,text = 'Copy',bg = 'black',padx = 54,fg = 'white',command = copy).pack(side = 'right')
