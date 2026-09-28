import mysql.connector

# create connection
con = mysql.connector.connect(host="localhost",user="root",password="root")
c=con.cursor()
# create db
c.execute("create database shop")
print("Database file created")
con = mysql.connector.connect(host="localhost",user="root",password="root",database="shop")
c=con.cursor()
# create table
c.execute('''
    create table Product(product_id int not null primary key,
    name varchar(10),
    brand varchar(10),
    category varchar(20),
    price int,
    stock int)''')
print("table created successfully")
def create():
    product_id=int(input("enter id:"))
    name=input("Enter name:")
    brand=input("enter brand:")
    category=input("enter category:")
    price=int(input("enter price:"))
    stock=int(input("enter stocks:"))
    query="insert into Product(product_id,name,brand,category,price,stock)values(%s,%s,%s,%s,%s,%s)"
    data=(product_id,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
    print("data inserted")
def get():
    query="select * from Product"
    c.execute(query)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No records found")

def retrieve():
    id=int(input("enter the product id:"))
    query=" select * from Product where product_id=%s"
    data=(id,)
    c.execute(query,data)
    records=c.fetchone()
    if records:
            print(records)
    else:
        print("No records found")
#
#
def update():
    id=int(input("enter the product id:"))
    stocks=int(input("enter the new stocks:"))
    query="update Product set stock=%s where product_id=%s"
    data=(stocks,id)
    c.execute(query,data)
    con.commit()
    print("updated")

def delete():
    id=int(input("enter the product id:"))
    query="delete from Product where product_id=%s"
    data=(id,)
    c.execute(query,data)
    con.commit()
    print("deleted")


while (1):
    print("Menu Driven")
    print("1.Add product details")
    print('2.Read all products')
    print('3.Search a product')
    print('4.Update stock')
    print('5.Delete product')

    ch = int(input("Enter choice:"))

    if ch == 1:
        create()
    elif ch == 2:
        get()
    elif ch == 3:
        retrieve()
    elif ch == 4:
        update()
    elif ch == 5:
        delete()
    else:
        exit()