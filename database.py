
import mysql
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "",
    database = "login"
)

# create a cursor
cursor = con.cursor()

# admin login function
def login(arg):
    try:
        cursor.execute('SELECT * FROM admin WHERE username = %s and Password = %s', arg)
        return cursor.fetchone()

    except:
        return False

def addclient(arg):
    # print(arg)
    try:
        cursor.execute('INSERT into client (name,Address,Contact) VALUES (%s,%s,%s)',arg)
        con.commit()
        return True

    except:
        return False

def selectClient(gup):
    try:
        # print("get",gup)
        cursor.execute('SELECT * FROM client WHERE id = %s',gup)
        return cursor.fetchall()     
    except:
        return False

def selectProduct(gup):
    try:
        # print("get",gup)
        cursor.execute('SELECT * FROM product WHERE id = %s',gup)
        return cursor.fetchall()     
    except:
        return False


def addProduct(arg):
    # print(arg)
    try:
        cursor.execute('INSERT into product (Name,Cost,stock) VALUES (%s,%s,%s)',arg)
        con.commit()
        return True
    except:
        return False

def updateProduct(arg):
    
    try:
        print("get",arg)
        cursor.execute('update product SET Name=%s, Cost=%s, stock=%s where id=%s',arg)
        con.commit()
        return True

    except:
        return False


def addbill(arg):
    print(arg)
    try:
        cursor.execute('INSERT into bill(clientID,productID,quantity,Per_PC_cost,totalAmount) VALUE(%s,%s,%s,%s,%s)',arg)
        con.commit()
        return True
    except:
        return False


def viewClient():
    try:
        cursor.execute('SELECT * FROM client order by id desc')
        return cursor.fetchall()
    except:
        return False

def viewBill():
    try:
        cursor.execute('SELECT * FROM bill order by id desc')
        return cursor.fetchall()
    except:
        return False

def dynamicClients():
    try:
        cursor.execute('SELECT Name FROM client')
        return cursor.fetchall()
    except:
        return False

def dynamicProduct():
    try:
        cursor.execute('SELECT Name FROM product')
        return cursor.fetchall()
    except:
        return False

def viewproduct():
    try:
        cursor.execute('SELECT * FROM product order by id desc')
        return cursor.fetchall()
    except:
        return False

def deleteclient(gup):
    try:
        print(gup)
        cursor.execute('DELETE FROM client WHERE id = %s',gup)
        con.commit()
        return True

    except:
        return False

def updateclient(gup):
    try:
        print("this",gup)
        cursor.execute('update client SET name=%s, Address=%s, Contact=%s where id=%s',gup)
        con.commit()
        # print(gup)
        return True

    except:
        return False


def deleteproduct(gup):
    try:
        print('delete',gup)
        cursor.execute('DELETE FROM product WHERE id = %s',gup)
        con.commit()
        return True

    except:
        return False



def singleBill(id):
    try:
        cursor.execute('SELECT * FROM bill where id = %s', id)
        return cursor.fetchone()
    except: 
        return False
























