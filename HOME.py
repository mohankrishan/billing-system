import email
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ADDBILL
import addClient
import LOGIN
import AddProduct
import ManageClient
import ManageProduct
import viewBill
from tkinter import ttk
import database
class AdminNav:
        def AddBill(self):
                self.root.destroy()
                obj = ADDBILL.AddBill()
                obj.firstFrame()
        def __init__(self):
                self.root = Tk()
                self.root.title("HOME")
                

                        # to get the width and height of your computer screen
                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                # 800 x 500 is the size of your screen

                self.width = int((self.fullwidth-900)/2)
                self.height=int((self.fullheight-574)/7)

                s = "900x574+" +str(self.width)+ "+" +str(self.height)
                self.root.geometry(s)
                self.root.resizable(width=False, height = False)
        
                self.menu=Menu()
                
                self.CLIENT = Menu(self.menu)
                self.menu.add_cascade(label= "CLIENT" , menu=self.CLIENT)
                self.CLIENT.add_command(label="Add",command=self.openAddClient)
                self.CLIENT.add_command(label="Manage",command=self.openManageClient)

                self.PRODUCT = Menu(self.menu)
                self.menu.add_cascade(label=  "PRODUCT", menu=self.PRODUCT)
                self.PRODUCT.add_command(label="Add Product",command=self.openAddProduct)
                self.PRODUCT.add_command(label = "Manage Product",command=self.openManageProduct)

                self.BILLING = Menu(self.menu)
                self.menu.add_cascade(label = "BILLING", menu = self.BILLING)
                self.BILLING.add_command(label="Add Bill",command=self.AddBill) 
                self.BILLING.add_command(label="View Bill",command=self.openviewBill)

                self.menu.add_command(label = "LOGOUT",command=self.root.quit)



                self.root.config(menu= self.menu)

        
        def navframe(self):
                self.navfra = Frame(self.root)
                self.navfra.place(x=0, y=0, width="900", height="574")
                self.root.resizable(height=False, width=False)
                

                self.image = Image.open("images/bll2.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.navfra, image=self.bgImg,bg = "#ffffff")
                self.bgLabel.place(x = 0, y = 0, width = "900", height = "574")

                self.lab1=Label(self.navfra,text="Total Client  :",anchor=E,fg="orange",bg="#ffffff")
                self.lab1.place(x=500,y=100,width="200",height="30")
                self.lab1.config(font=("Forte",20))

                self.lab1=Label(self.navfra,text="Total Product  :",anchor=E,fg="orange",bg="#ffffff")
                self.lab1.place(x=500,y=150,width="200",height="30")
                self.lab1.config(font=("Forte",20))

                self.lab1=Label(self.navfra,text="Total Bill   :",anchor=E,fg="orange",bg="#ffffff")
                self.lab1.place(x=530,y=200,width="150",height="30")
                self.lab1.config(font=("Forte",20))

                count = 0
                for data in database.viewClient():
                        # print(data)
                        count+=1
                print(count)

                self.countClient=Label(self.navfra,text=count,anchor=E,fg="orange",bg="#ffffff")
                self.countClient.place(x=700,y=100,width="40",height="30")
                self.countClient.config(font=("Forte",20)) 

                count = 0
                for data in database.viewproduct():
                        # print(data)
                        count+=1
                print(count)

                self.countClient=Label(self.navfra,text=count,anchor=E,fg="orange",bg="#ffffff")
                self.countClient.place(x=700,y=150,width="40",height="30")
                self.countClient.config(font=("Forte",20))

                count = 0
                for data in database.viewBill():
                        # print(data)
                        count+=1
                print(count)

                self.countClient=Label(self.navfra,text=count,anchor=E,fg="orange",bg="#ffffff")
                self.countClient.place(x=700,y=200,width="40",height="30")
                self.countClient.config(font=("Forte",20))
                

                self.root.mainloop()

        def openAddClient(self):
                self.root.destroy()
                addClientObj = addClient.AddClient()
                addClientObj.firstFrame()

        def openAddProduct(self):
                self.root.destroy()
                addproducttObj = AddProduct.Addproduct()
                addproducttObj.firstFrame()

        def openAddBill(self):
                self.root.destroy()
                addbillObj = ADDBILL.AddBill()
                addbillObj.firstFrame()       

        def openManageClient(self):
                self.root.destroy()
                manageclint = ManageClient.manageClient()
                manageclint.frFrame()

        def openManageProduct(self):
                self.root.destroy()
                manageclint = ManageProduct.Manageproduct()
                manageclint.firstFrame()

        def openviewBill(self):
                self.root.destroy()
                manageclint = viewBill.Viewbill()
                manageclint.firstFrame()

        

        

if __name__=='__main__':
    obj1 = AdminNav()
    obj1.navframe()
    obj1.firstFrame()
        




