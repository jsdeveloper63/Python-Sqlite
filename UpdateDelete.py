import sqlite3


#Create the database
conn = sqlite3.connect("Electricity.db")
#Cursor method is used to go through the database
c = conn.cursor()

#Deletes the Table completely
#c.execute("DROP TABLE electricity")

#Updates the rows of column date  
#c.execute("UPDATE electricity SET date = '02-02-2020'"+
#          "WHERE date == 0")

#c.execute("UPDATE electricity SET class == 'MIDDLE' WHERE "+
#          "nswprice < 0.05 AND nswdemand < 0.2")

#Deletes the entire day column 
#c.execute("DELETE FROM electricity day"


#csvfile.close()
conn.commit()
c.close()
conn.close()
             
