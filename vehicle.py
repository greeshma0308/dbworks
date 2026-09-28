import mysql.connector
class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(host="localhost", user="root", password="root",database="motor")
        self.cursor=self.connection.cursor()
        print("Successfully connected")
    def list(self):
        #reading all records from db table
        query="select * from vehicle"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                    print(row)
        else:
            print("No records found")
    def create(self,id,model,brand,type,price,year):
        query="insert into vehicle(id,model,brand,type,price,year)values(%s,%s,%s,%s,%s,%s)"
        data=(id,model,brand,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data inserted successfully")
    def retrieve(self,id):
        query = " select * from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        records = self.cursor.fetchone()
        if records:
            print(records)
        else:
            print("No records found")
    def update(self,id,model,brand,type,price,year):
        query ="update vehicle set model=%s, brand=%s, type=%s, price=%s, year=%s where id=%s"
        data = (model,brand,type,price,year,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("updated")
    def delete(self,id):
        query = "delete from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("deleted")
        else:
            print("no records found")
vehicle_instance=VehicleListCreateRetrieveUpdateDelete()
vehicle_instance.list()
vehicle_instance.create('2','punch','tata','car','1000000',2022)
vehicle_instance.retrieve(2)
vehicle_instance.update(2,"alto","maruti suzuki",'car',500000,2013)
vehicle_instance.delete(1)