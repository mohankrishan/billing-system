import email
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import HOME
import database
from tkinter import ttk
from tkcalendar import Calendar

class AddBill:

        def __init__(self):
                self.root = Tk()
                self.root.title("ADD_BILL")
                

                        # to get the width and height of your computer screen
                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                # 800 x 500 is the size of your screen

                self.width = int((self.fullwidth-800)/2)
                self.height=int((self.fullheight-474)/7)

                s = "900x574+" +str(self.width)+ "+" +str(self.height)



                self.root.geometry(s)
                self.root.resizable(width=False, height = False)

        def mul(self):
                self.ent5.delete(0, 'end')
                if ((self.ent3.get() != '') and (self.ent4.get() != '')):
                        quan = int(self.ent3.get())
                        per = int(self.ent4.get())
                        print(quan, per)
                        sum =quan * per
                        print(sum)
                        # self.ent5.config(Value = sum)
                        self.ent5.insert(0, sum)
                        return sum
                else:
                        return 0

        def firstFrame(self):
                self.mainFrame = Frame(self.root)
                self.mainFrame.config(bg="#e4e4e4")
                self.mainFrame.place(x = 0, y= 0 , width="900", height="574")

                self.image = Image.open("images/bill-iconsmall.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg)
                self.bgLabel.config(bg='#e4e4e4')
                self.bgLabel.place(x = 250, y = -200,width="300",height="600")



                self.lab=Label(self.mainFrame,text="Clint ID   :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab.place(x=300,y=200,width="180",height="30")
                self.lab.config(font=("Modern No. 20",20))
                
                self.lab1=Label(self.mainFrame,text="Product ID :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab1.place(x=300,y=250,width="180",height="30")
                self.lab1.config(font=("Modern No. 20",20))

                # self.lab2=Label(self.mainFrame,text="Date        :-",anchor=E,fg="black",bg="#e4e4e4")
                # self.lab2.place(x=300,y=300,width="180",height="30")
                # self.lab2.config(font=("Modern No. 20",20))

                self.lab3=Label(self.mainFrame,text="Quantity    :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab3.place(x=300,y=350,width="180",height="30")
                self.lab3.config(font=("Modern No. 20",20))

                self.lab4=Label(self.mainFrame,text="Per Pc Cost   :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab4.place(x=300,y=400,width="180",height="30")
                self.lab4.config(font=("Modern No. 20",20))

                self.lab5=Label(self.mainFrame,text="Total Amount :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab5.place(x=300,y=450,width="180",height="30")
                self.lab5.config(font=("Modern No. 20",20))

                self.client = StringVar()
                self.client = (database.dynamicClients())
                self.selbox = ttk.Combobox(self.mainFrame,state="readonly",textvariable=self.client,value=self.client)
                self.selbox.place(x = 500,y=200,width="150",height="30")
                self.selbox.bind('<<ComboboxSelected>>',self.onDropChage)

                

                self.product = StringVar()
                self.product = (database.dynamicProduct())
                self.selbox1 = ttk.Combobox(self.mainFrame,state="readonly",textvariable=self.product,value=self.product)
                self.selbox1.place(x = 500,y=250,width="150",height="30")
                self.selbox1.bind('<<ComboboxSelected>>',self.onDropChage)

                # self.cal = Calendar(self.mainFrame, selectmode = 'day', year = 2022, month = 7, day = 13)

                # self.cal.place(x = 500, y = 300, width = "150", height = "30")

                # self.date=StringVar()
                # self.ent2=Entry(self.mainFrame,textvariable=self.date)
                # self.ent2.place(x=500,y=300,width="150",height="30")
                
                self.Quantity=StringVar()
                self.ent3=Entry(self.mainFrame,textvariable=self.Quantity, validate= "focusout", validatecommand=self.mul)
                self.ent3.place(x=500,y=350,width="150",height="30")

                self.PerPcCost=StringVar()
                self.ent4=Entry(self.mainFrame,textvariable=self.PerPcCost, validate= "focusout", validatecommand=self.mul)
                self.ent4.place(x=500,y=400,width="150",height="30")


                self.TotalAmount=StringVar()
                # a = self.mul()
                self.ent5=Entry(self.mainFrame, textvariable= self.TotalAmount, validate= "focusout", validatecommand=self.mul,bg="white")
                self.ent5.place(x=500,y=450,width="150",height="30")

                # self.totalLabel = Label(self.mainFrame, text=self.mul())
                # self.totalLabel.place(x = 500, y = 450, width="150", height="30")

                self.submitButton = Button(self.mainFrame, text = "Proceed",fg="black",bg="#1B7BF4",command=self.abc)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 450, y = 500, width = "90", height="40")

                self.submitButton = Button(self.mainFrame, text = "Back",fg="#2F2F4A",bg="#F15630",command=self.openHOME)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 800, y = 10, width = "90", height="40")





                self.root.mainloop()
        
        def onDropChage(self,abc):
                # messagebox.showinfo("Hey",self.client.get())
                pass
        def onDropChage(self,abc):
                # messagebox.showinfo("Hey",self.product.get())
                pass

        def openHOME(self):
                self.root.destroy()
                addClientObj = HOME.AdminNav()
                addClientObj.navframe()

        


        
        def abc(self):
                self.data = (   
                                self.selbox.get(),
                                self.selbox1.get(),
                                # self.ent2.get(),
                                # self.cal.get_date(),
                                self.ent3.get(),
                                self.ent4.get(),
                                self.ent5.get()
                                         
                        )
                

                # if (self.client.get() == ''):
                #         messagebox.showinfo('Alert', 'Please enter Clint ID.')
                # elif (self.product.get() == ''):
                #         messagebox.showinfo('Alert', 'Please enter item Product ID.')
                
                # if (self.ent2.get() == ''):
                #         messagebox.showinfo('Alert', 'Please enter Date.')
                        
                if (not(self.ent3.get().isdigit())):
                        messagebox.showinfo('Alert', 'Please enter only digits in Quantity.')
                elif (self.ent3.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Quantity.')  
                elif (not(self.ent4.get().isdigit())):
                        messagebox.showinfo('Alert', 'Please enter only digits in Total amount.')        
                elif (self.ent5.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Total amount.')
                
                else:
                        res = database.addbill(self.data)
                        print(res)
                        if res:
                                messagebox.showinfo('Success', 'Add Successfully')
                                self.root.destroy()
                                homeObj = HOME.AdminNav()
                                homeObj.navframe()
                        else:
                                messagebox.showinfo('Alert', 'Invalid.')



if __name__ == '__main__':
    ovj=AddBill()
    ovj.firstFrame()