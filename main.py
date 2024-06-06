import tkinter as tk
from CTkMenuBar import *

from PIL import ImageTk, Image
from tkinter.messagebox import *
import customtkinter
from PIL.ImageTk import PhotoImage


def handler(key):
    if key==1:
        e1.insert(len(e1.get()),"1")
    elif key==2:
        e1.insert(len(e1.get()),"2")
    elif key==3:
        e1.insert(len(e1.get()), "3")
    elif key == 4:
        e1.insert(len(e1.get()), "4")
    elif key == 5:
        e1.insert(len(e1.get()), "5")
    elif key == 6:
        e1.insert(len(e1.get()), "6")
    elif key == 7:
        e1.insert(len(e1.get()), "7")
    elif key == 8:
        e1.insert(len(e1.get()), "8")
    elif key == 9:
        e1.insert(len(e1.get()), "9")
    elif key == 0:
        e1.insert(len(e1.get()), "0")
    elif key == '=':
        r1=str(eval(e1.get()))
        if '.' in r1:
            ra = float(r1)
            if ra % 2.0 == 1.0:
                result = int(ra)
            else:
                result = float(r1)
        else:
            result = int(r1)
        e1.delete(0,tk.END)
        e1.insert(0,str(result))
    elif key == '+':
        e1.insert(len(e1.get()), "+")
    elif key == '*':
        e1.insert(len(e1.get()), "*")
    elif key == '-':
        e1.insert(len(e1.get()), "-")
    elif key == '/':
        e1.insert(len(e1.get()), "/")
    elif key == '.':
        e1.insert(len(e1.get()), ".")
    elif key == '⌦':
        e1.delete(e1.index('end') - 1)
    elif key == 'C':
        e1.delete(0,len(e1.get()))


def aboutus():
    tk.messagebox.showinfo("About", "Calculadora is a Open Source Calculator Application.\n Developed by Akib Khan ")

customtkinter.set_window_scaling(1.8)
customtkinter.set_widget_scaling(1.8)
root = customtkinter.CTk()
root.title('Calculadora')
root.geometry('180X250')
root.maxsize(160,200)


customtkinter.set_appearance_mode("system")
img = PhotoImage(file='icon.png')
root.iconphoto(False,img)
menubar = tk.Menu()
about = tk.Menu(menubar, tearoff=False)
about.add_command(label="About",
                  command=aboutus)
menubar.add_cascade(menu=about, label="About",command=aboutus)

root.config(menu=menubar)



e1= customtkinter.CTkEntry(root,width=140)
e1.grid(row=0,column=0,columnspan=4, pady = 15,padx=6)
button = customtkinter.CTkButton(root,text='1',width=25,command=lambda:handler(1))
button.grid(row=4,column =0)

button = customtkinter.CTkButton(root,text='2',width=25,command=lambda:handler(2))
button.grid(row=4,column =1)

button = customtkinter.CTkButton(root,text='3',width=25,command=lambda:handler(3))
button.grid(row=4,column =2)

button = customtkinter.CTkButton(root,text='4',width=25,command=lambda:handler(4))
button.grid(row=3,column =0)

button = customtkinter.CTkButton(root,text='5',width=25,command=lambda:handler(5))
button.grid(row=3,column =1)
button = customtkinter.CTkButton(root,text='6',width=25,command=lambda:handler(6))
button.grid(row=3,column =2)
button = customtkinter.CTkButton(root,text='7',width=25,command=lambda:handler(7))
button.grid(row=2,column =0)
button = customtkinter.CTkButton(root,text='8',width=25,command=lambda:handler(8))
button.grid(row=2,column =1)
button = customtkinter.CTkButton(root,text='9',width=25,command=lambda:handler(9))
button.grid(row=2,column =2)
button = customtkinter.CTkButton(root,text='0',width=25,command=lambda:handler(9))
button.grid(row=5,column =0)
button = customtkinter.CTkButton(root,text='=',width=25,command=lambda:handler('='))
button.grid(row=5,column=3)
button = customtkinter.CTkButton(root,text='+',width=25,command=lambda:handler('+'))
button.grid(row=2,column =3)
button = customtkinter.CTkButton(root,text='*',width=25,command=lambda:handler('*'))
button.grid(row=3,column =3)
button = customtkinter.CTkButton(root,text='-',width=25,command=lambda:handler('-'))
button.grid(row=4,column =3)
button = customtkinter.CTkButton(root,text='.',width=25,command=lambda:handler('.'))
button.grid(row=5,column =1)
button = customtkinter.CTkButton(root,text='/',width=25,command=lambda:handler('/'))
button.grid(row=5,column =2)
button = customtkinter.CTkButton(root,text='⌦',width=25,command=lambda:handler('⌦'))
button.grid(row=1,column =3)
button = customtkinter.CTkButton(root,text='C',width=25,command=lambda:handler('C'))
button.grid(row=1,column =2)


root.mainloop()