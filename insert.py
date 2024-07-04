import sqlite3

conn = sqlite3.connect("test.db")
print("Success")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'John','Maina',56,250000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Peligro','Sanchez',20,100000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Elsa','Njoki',28,50000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Jane','Kamau',48,28000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Joy','Karanja',35,30000.00)")

conn.commit()
print("Successfully inserted records")
conn.close()

