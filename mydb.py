import mysql.connector

# con = mysql.connector.connect(host="localhost",user="root",password="root")
# c=con.cursor()
#
# # c.execute(command)
# # create database file
#
# c.execute("create database school_db")
# print("Database file created")

con = mysql.connector.connect(host="localhost",user="root",password="root",database="school_db")
c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,name varchar(10),age int,place varchar(10),phone varchar(20),total_mark int)''')
# print("table created successfully")

# c.execute('''
# insert into student(roll_no,name,age,place,phone,total_mark)values
# (1,'abin',22,'kylm','153432315',89),
# (2,'arun',23,'hpd','543443531',72),
# (3,'lena',20,'kollam','34543746',55),
# (4,'lekshmi',24,'kattanam','583543584',40)
# ''')

# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
# data=(5,'kiran',21,'ekm','648586553',92)
# c.execute(query,data)
# con.commit()
# print("data inserted")

#read
# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No records found")

#  #read all attributes of a student with rollno =roll no entered by the user
# no=int(input("enter the roll no:"))
# query=" select * from student where roll_no=%s"
# data=(no,)
# c.execute(query,data)
# records=c.fetchone()
# if records:
#         print(records)
# else:
#     print("No records found")

 #update mark of a student with rollno=rollno entered by user
# no=int(input("enter the roll no:"))
# mark=int(input("enter the new marks:"))
# query="update student set total_mark=%s where roll_no=%s"
# data=(mark,no)
# c.execute(query,data)
# con.commit()
# print("updated")

 #delete a record with rollno=rollno entered by user
# no=int(input("enter the roll no:"))
# query="delete from student where roll_no=%s"
# data=(no,)
# c.execute(query,data)
# con.commit()
# print("deleted")

#create a new record using values entered by user
roll_no=int(input("enter roll no:"))
name=input("enter name:")
age=int(input("enter age:"))
place=input("enter place:")
phone=input("enter phone:")
total_mark=int(input("enter mark:"))
query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
data=(roll_no,name,age,place,phone,total_mark)
c.execute(query,data)
con.commit()
print("data inserted")