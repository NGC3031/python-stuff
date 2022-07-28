# To test a postgres setup
import psycopg2
import sys

con = None

try:
    con=psycopg2.connect(database="testdb", user = "postgres", password = "scott", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    #cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    #cur.execute("INSERT INTO Products VALUES(1,'Milk',5)")
    #cur.execute("INSERT INTO Products VALUES(2,'Sugar',7)")
    #cur.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
    #cur.execute("INSERT INTO Products VALUES(4,'Bread',5)")
    #cur.execute("INSERT INTO Products VALUES(5,'Oranges',3)")
    #con.commit()

    cur.execute("SELECT * FROM Products")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))

except psycopg2.DatabaseError as e:
    if con:
        con.rollback()
    
    print ('Error %s' % e)    
    sys.exit(1)
    
finally:   
    if con:
        con.close()
