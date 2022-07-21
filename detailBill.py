from ast import If
from configparser import ExtendedInterpolation
import email
from email import message
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import LOGIN
import HOME
import database
from tkinter import ttk
import viewBill

class DetailBill:
    def __init__(self):
                self.root = Tk()
                self.root.title("DETAIL_BILL")
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

    def firstFrame(self, id):
    
                res = database.singleBill(id)
                print(res)
                if res:
                    self.client = res[1]
                    self.dates = res[3]
                    self.totalCost = res[6]
                    self.product = res[2]
                    self.quantity = res[4]
                    self.cost = res[5]
                else:
                    messagebox.showinfo('Something went wrong.')
                    self.root.destroy()
                    obj = viewBill.Viewbill()
                    obj.firstFrame()

                self.mainFrame = Frame(self.root)
                self.mainFrame.place(x = 0, y= 0 , width="900", height="574")

                self.image = Image.open("images/box6.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg,bg = "#D4D4D4")
                self.bgLabel.place(x = 0, y = 0, width = "900", height = "574")

                self.image1 = Image.open("images/tool.jpg")
                self.bgImg1 = ImageTk.PhotoImage(self.image1)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg1,bg = "#D4D4D4")
                self.bgLabel.place(x = 30, y = 20, width = "130", height = "130")


                self.lab=Label(self.mainFrame,text="R.S. Engineering Works",anchor=E,fg="black",bg="#D4D4D4")
                self.lab.place(x=200,y=20,width="400",height="70")
                self.lab.config(font=("Modern No. 20",25,"bold"))

                self.lab=Label(self.mainFrame,text="JALANDHAR",anchor=E,fg="black",bg="#D4D4D4")
                self.lab.place(x=350,y=80,width="150",height="70")
                self.lab.config(font=("Modern No. 20",15,"bold"))

                self.lab=Label(self.mainFrame,text="TO :",anchor=W,fg="black",bg="#D4D4D4")
                self.lab.place(x=70,y=170,width="50",height="70")
                self.lab.config(font=("Modern No. 20",20,"bold"))

                self.lab=Label(self.mainFrame,text=self.client,anchor=W,fg="black",bg="#D4D4D4")
                self.lab.place(x=190,y=180,width="200",height="50")
                self.lab.config(font=("Modern No. 20",20,"bold"))
                
                self.lab=Label(self.mainFrame,text="DATE :",anchor=W,fg="black",bg="#D4D4D4")
                self.lab.place(x=70,y=230,width="100",height="70")
                self.lab.config(font=("Modern No. 20",20,"bold"))

                self.lab=Label(self.mainFrame,text=str(self.dates),anchor=W,fg="black",bg="#D4D4D4")
                self.lab.place(x=200,y=240,width="200",height="50")
                self.lab.config(font=("Modern No. 20",20,"bold"))

                self.lab=Label(self.mainFrame,text="TOTAL",anchor=E,fg="black",bg="#D4D4D4")
                self.lab.place(x=130,y=500,width="300",height="70")
                self.lab.config(font=("Modern No. 20",25,"bold"))

                self.tr = ttk.Treeview(self.mainFrame, columns=('PRODUCT', 'QUANITITY', 'COST/Pc', 'TOTAL'), selectmode="extended")

               

                self.tr.heading('#0', text="PRODUCT")
                self.tr.column('#0', minwidth=0, width=150, stretch=NO)

                self.tr.heading('#1', text="QUANITITY")
                self.tr.column('#1', minwidth=0, width=150, stretch=NO)

                self.tr.heading('#2', text="COST/Pc")
                self.tr.column('#2', minwidth=0, width=150, stretch=NO)

                self.tr.heading('#3', text="TOTAL")
                self.tr.column('#3', minwidth=0, width=150, stretch=NO)
                
                self.tr.insert('', 0, values=(self.product, self.quantity, self.cost, self.totalCost))
                # self.tr.bind('<Double-Button-1>', self.action)
                # for i in database.singleBill(id):
                #     print(i)
                #     self.tr.insert('', 0, text=i[0], values=(i[2], i[4], i[5], i[6]))
                self.tr.place(x=50, y=350 ,width="670", height="100")

                self.text=StringVar()
                self.ent1=Label(self.mainFrame,text = self.totalCost)
                self.ent1.place(x=470,y=515,width="130",height="40")



                self.root.mainloop()



    

if __name__ == '__main__':
        loginObj = DetailBill()
        loginObj.firstFrame('view')