import sys
import socket
import server
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 21100                    # Reserve a port for your service.

s.connect((host, port))


try:
 import Tkinter as tk
except ImportError:
 import tkinter as tk

try:
 import ttk
 py3 = False
except ImportError:
 import tkinter.ttk as ttk
 py3 = True

import client_support

def vp_start_gui():
 '''Starting point when module is the main routine.'''
 global val, w, root
 root = tk.Tk()
 top = Toplevel1 (root)
 client_support.init(root, top)
 root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
 '''Starting point when module is imported by another program.'''
 global w, w_win, rt
 rt = root
 w = tk.Toplevel (root)
 top = Toplevel1 (w)
 client_support.init(w, top, *args, **kwargs)
 return (w, top)

def destroy_Toplevel1():
 global w
 w.destroy()
 w = None

class Toplevel1:
 def __init__(self, top=None):
     '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
     _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
     _fgcolor = '#000000'  # X11 color: 'black'
     _compcolor = '#d9d9d9' # X11 color: 'gray85'
     _ana1color = '#d9d9d9' # X11 color: 'gray85'
     _ana2color = '#ececec' # Closest X11 color: 'gray92'

     top.geometry("600x450+331+185")
     top.minsize(120, 1)
     top.maxsize(1370, 749)
     top.resizable(1, 1)
     top.title("Client")
     top.configure(background="#d9d9d9")

     self.Canvas1 = tk.Canvas(top)
     self.Canvas1.place(relx=0.1, rely=0.089, relheight=0.74, relwidth=0.772)
     self.Canvas1.configure(background="#d9d9d9")
     self.Canvas1.configure(borderwidth="2")
     self.Canvas1.configure(insertbackground="black")
     self.Canvas1.configure(relief="ridge")
     self.Canvas1.configure(selectbackground="#c4c4c4")
     self.Canvas1.configure(selectforeground="black")

     self.Label1 = tk.Label(self.Canvas1)
     self.Label1.place(relx=0.086, rely=0.15, height=21, width=78)
     self.Label1.configure(background="#d9d9d9")
     self.Label1.configure(disabledforeground="#a3a3a3")
     self.Label1.configure(foreground="#000000")
     self.Label1.configure(text='''Request File :''')
     
     self.Entry1 = tk.Entry(self.Canvas1)
     self.Entry1.place(relx=0.37, rely=0.137,height=20, relwidth=0.448)
     self.Entry1.configure(background="white")
     self.Entry1.configure(disabledforeground="#a3a3a3")
     self.Entry1.configure(font="TkFixedFont")
     self.Entry1.configure(foreground="#000000")
     self.Entry1.configure(insertbackground="black")
     
     
     self.Button1 = tk.Button(self.Canvas1)
     self.Button1.place(relx=0.375, rely=0.275, height=30, width=130)
     self.Button1.configure(activebackground="#ececec")
     self.Button1.configure(activeforeground="#000000")
     self.Button1.configure(background="#d9d9d9")
     self.Button1.configure(disabledforeground="#a3a3a3")
     self.Button1.configure(foreground="#000000")
     self.Button1.configure(highlightbackground="#d9d9d9")
     self.Button1.configure(highlightcolor="black")
     self.Button1.configure(pady="0")
     self.Button1.configure(text='''Send''',command=lambda: server.function(self.Entry1.get()))


     
     self.Message1 = tk.Message(self.Canvas1)
     self.Message1.place(relx=0.194, rely=0.781, relheight=0.069
             , relwidth=0.648)
     self.Message1.configure(background="#d9d9d9")
     self.Message1.configure(foreground="#000000")
     self.Message1.configure(highlightbackground="#d9d9d9")
     self.Message1.configure(highlightcolor="black")
     self.Message1.configure(width=300)

     self.Label2 = tk.Label(self.Canvas1)
     self.Label2.place(relx=0.475, rely=0.511, height=21, width=38)
     self.Label2.configure(background="#d9d9d9")
     self.Label2.configure(disabledforeground="#a3a3a3")
     self.Label2.configure(foreground="#000000")
     self.Label2.configure(text='''Status''')
s.close()

if __name__ == '__main__':
 vp_start_gui()



