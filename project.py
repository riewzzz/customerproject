import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="game"
)

mycursor = mydb.cursor()

def createTable():
    mycursor.execute("create table if not exists customers (id int auto_increment primary key, name varchar(255), address varchar(255))")

createTable()

def existsCustomers(name, address):
    query = "select count(*) from customers where name='{}'".format(name)
    print(query)
    mycursor.execute(query)
    
    myresult = mycursor.fetchall()
    
    
    print("myresluts=")
    print(myresult)
    print("myresult[0]=")
    print(myresult[0])
    print("myresult[0][0]")
    
    
    count = myresult[0][0]
    print(count)
    
    if count == 0:
        
        sql = "insert into customers (name, address) values (%s, %s)"
        val = (name, address)
        mycursor.execute(sql, val)
        
        mydb.commit()
        
        print(mycursor.rowcount, "records inserted.")
    else:
        print("Duplicate")
        
    
answer = ''
      
while answer != "none":

    answer = input("Please insert name of customr: ")
    
    if answer !=  "none":
        name = answer
    
        address = input("Please insert address: ")

        existsCustomers(name, address)
