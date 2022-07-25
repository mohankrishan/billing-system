from ast import If
from configparser import ExtendedInterpolation
import email
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from turtle import width
from PIL import ImageTk, Image
import database
import HOME
from tkinter import ttk
import EditProduct 


class Manageproduct:

        def __init__(self):
                self.root = Tk()
                self.root.title("MANAGE_PRODUCT")
                self.root.config(bg="gray")

                        # to get the width and height of your computer screen
                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                # 800 x 500 is the size of your screen

                self.width = int((self.fullwidth-800)/2)
                self.height=int((self.fullheight-474)/7)

                s = "900x574+" +str(self.width)+ "+" +str(self.height)



                self.root.geometry(s)
                self.root.resizable(width=False, height = False)

        def firstFrame(self):

                # create frame
                self.mainFrame = Frame(self.root)
                self.mainFrame.place(x = 0, y= 0 , width="900", height="574")

                
                self.submitButton = Button(self.mainFrame, text = "Back",fg="#2F2F4A",bg="#F15630",command=self.openHOME)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 800, y = 10, width = "90", height="40")

                self.tr = ttk.Treeview(self.mainFrame, columns=('Id', 'Name', 'Cost','Stock','Delete','Edit'), selectmode="extended")
                self.tr.heading('#0', text="ID")
                self.tr.column('#0', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#1', text="Name")
                self.tr.column('#1', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#2', text="Cost")
                self.tr.column('#2', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#3', text="Stock")
                self.tr.column('#3', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#4', text="Delete")
                self.tr.column('#4', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#5', text="Edit")
                self.tr.column('#5', minwidth=0, width=100, stretch=NO)

                j = 0
                print(database.viewproduct)
                for i in database.viewproduct():
                        self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3],'Delete','Edit'))
                j += 1
                # create doble action button
                self.tr.bind('<Double-Button-1>', self.actions)
                self.tr.place(x=0, y=0,width="900", height="574")
                self.submitButton = Button(self.mainFrame, text = "Back",fg="#2F2F4A",bg="#F15630",command=self.openHOME)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x =800, y = 20, width = "90", height="40")
                self.root.mainloop()

        def actions(self, e):
                # get the values of the selected rows\\
                tt = self.tr.focus()

                # get the column id
                col = self.tr.identify_column(e.x)
                # print(col)
                # print(self.tr.item(tt))

                gup = (
                self.tr.item(tt).get('text'),
                )
                if col == '#4':
                        res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
                        if res:
                                rs = database.deleteproduct(gup)
                                if rs:
                                        messagebox.showinfo("ALERT", "Suuccessfully Deleted")
                                self.root.destroy()
                                obj = Manageproduct()
                                obj.firstFrame()
                if col == '#5':
                        self.root.destroy()
                        obj = EditProduct.editproduct()
                        obj.firstFrame(gup)



                self.root.mainloop()


        def openHOME(self):
                self.root.destroy()
                addClientObj = HOME.AdminNav()
                addClientObj.navframe()

                
                

if __name__ == '__main__':
        Obj = Manageproduct()
        Obj.firstFrame()
        Obj.root.mainloop()