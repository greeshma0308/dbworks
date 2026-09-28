import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(host="localhost", user="root", password="root",database="library_db")
        self.cursor=self.connection.cursor()
        print("Successfully connected")
    def list(self):
        #reading all records from db table
        query="select * from book"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                    print(row)
        else:
            print("No records found")
    # def create(self,title,author,price,pages,language):
    #     query="insert into book(title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
    #     data=(title,author,price,pages,language)
    #     self.cursor.execute(query,data)
    #     self.connection.commit()
    #     print("Data inserted successfully")
    def retrieve(self,id):
        query = " select * from book where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        records = self.cursor.fetchone()
        if records:
            print(records)
        else:
            print("No records found")
    def update(self,id,title,author,price,pages,language):
        query ="update book set title=%s, author=%s, price=%s, pages=%s, language=%s where id=%s"
        data = (title,author,price,pages,language,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("updated")
    def delete(self,id):
        query = "delete from book where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("deleted")
book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# # book_instance.create('Harry Potter and the order of phoenix','J K Rowling',800,600,'English')
# book_instance.retrieve(1)
book_instance.update(2,"harry potter","J K",750,650,"malayalam")
# book_instance.delete(1)