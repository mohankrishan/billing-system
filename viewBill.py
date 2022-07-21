from ast import If
from configparser import ExtendedInterpolation
import email
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import HOME
import database
from tkinter import ttk
import detailBill

class Viewbill:

        def __init__(self):
                self.root = Tk()
                self.root.title("VIEW_BILL")
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

                self.tr = ttk.Treeview(self.mainFrame, columns=('id','Clint ID', 'Product ID', 'Date','Quantity','Per Pc Cost','Total Amount', 'View'), selectmode="extended")
                self.tr.heading('#0', text="ID")
                self.tr.column('#0', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#1', text="Clint ID")
                self.tr.column('#1', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#2', text="Product ID")
                self.tr.column('#2', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#3', text="Date")
                self.tr.column('#3', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#4', text="Quantity")
                self.tr.column('#4', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#5', text="Per Pc Cost")
                self.tr.column('#5', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#6', text="Total Amount")
                self.tr.column('#6', minwidth=0, width=100, stretch=NO)

                self.tr.heading('#7', text="View")
                self.tr.column('#7', minwidth=0, width=100, stretch=NO)


                j = 0
                print(database.viewBill)
                for i in database.viewBill():
                        self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6], 'View'))
                j += 1
                # create doble action button
                self.tr.bind('<Double-Button-1>', self.actions)
                self.tr.place(x=0, y=0,width=900,height=574)

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

                if col == '#7':
                        self.root.destroy()
                        obj = detailBill.DetailBill()
                        obj.firstFrame(gup)



        def openHOME(self):
                self.root.destroy()
                addClientObj = HOME.AdminNav()
                addClientObj.navframe()

                
                

if __name__ == '__main__':
        Obj = Viewbill()
        Obj.firstFrame()