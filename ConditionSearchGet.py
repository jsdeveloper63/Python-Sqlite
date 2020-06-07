import sqlite3


#Create the database
conn = sqlite3.connect("Electricity.db")
#Cursor method is used to go through the database
c = conn.cursor()

#Select individual column from the table
#c.execute("SELECT period FROM electricity")

#Prints/Gives data from all columns 
#c.execute("SELECT * FROM electricity")
#data = c.fetchall()
#print(data)

#To Select some specific chunk of data
#Selects the 2 rows of data after offsetting / skipping the first 10 rows
#c.execute("SELECT * FROM electricity LIMIT 2 OFFSET 10")
#data = c.fetchall()
#print(data)

#Gives the data in order
#c.execute("SELECT * FROM electricity ORDER BY vicprice")
#data = c.fetchmany(size=20)
#print(data)

#Using ASCI / DESC print the data in ascending or descending order
#c.execute("SELECT * FROM electricity ORDER BY vicprice ASC")
#data = c.fetchone()
#print(data)

#To retreive distinct values in case we have replicate data
#c.execute("SELECT DISTINCT date FROM electricity")
#data = c.fetchall()
#for i in data:
#    print(data)


conn.commit()
c.close()
conn.close()
             
