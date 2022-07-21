from ast import If
from configparser import ExtendedInterpolation
import email
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import HOME
import database

class LoginWindow:

        def __init__(self):
                self.root = Tk()
                self.root.title("ADMIN - Login")

                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                self.width = int((self.fullwidth-900)/2)
                self.height=int((self.fullheight-574)/7)

                s = "900x574+" +str(self.width)+ "+" +str(self.height)

                self.root.geometry(s)
                self.root.resizable(width=False, height = False)
             
        def firstFrame(self):

                self.mainFrame = Frame(self.root)
                self.mainFrame.place(x = 0, y= 0 , width="900", height="574")

                self.image = Image.open("images/Billl.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg,bg = "gray")
                self.bgLabel.place(x = 0, y = 0, width = "900", height = "574")

                self.lab=Label(self.mainFrame,text="Username",anchor=E,fg="orange",bg="#F9F8FF")
                self.lab.place(x=200,y=200,width="150",height="30")
                self.lab.config(font=("Forte",20))
                
                self.lab1=Label(self.mainFrame,text="Password",anchor=E,fg="orange",bg="#F9F8FF")
                self.lab1.place(x=195,y=250,width="150",height="30")
                self.lab1.config(font=("Forte",20))

                self.user=StringVar()
                self.ent=Entry(self.mainFrame,textvariable=self.user)
                self.ent.place(x=450,y=200,width="150",height="30")

                self.passw=StringVar()
                self.ent1=Entry(self.mainFrame,textvariable=self.passw, show = "*")
                self.ent1.place(x=450,y=250,width="150",height="30")

                self.loginButton = Button(self.mainFrame, text = "Login",fg="#2F2F4A",bg="white", command = self.loginUser)
                self.loginButton.config(font = ("Forte",20,"bold"))
                self.loginButton.place(x = 350, y = 330, width = "80", height="40")

                self.root.mainloop()

        def loginUser(self):
                self.data = (
                        self.ent.get(),
                        self.ent1.get()
                )

                if (self.ent.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter your username.')
                elif (self.ent1.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter your password.')
                else:
                        res = database.login(self.data)
                        if res:
                                messagebox.showinfo('Success', 'Login Successfully')
                                self.root.destroy()
                                homeObj = HOME.AdminNav()
                                homeObj.navframe()
                        else:
                                messagebox.showinfo('Alert', 'Invalid username and/or password.')

if __name__ == '__main__':
        loginObj = LoginWindow()
        loginObj.firstFrame()

