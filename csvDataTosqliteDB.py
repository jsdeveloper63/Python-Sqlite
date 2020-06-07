import sqlite3
import csv


#Create the database
conn = sqlite3.connect("Electricity.db")
#Cursor method is used to go through the database
c = conn.cursor()

#Create the table
c.execute('CREATE TABLE electricity(date Real,'+
                                   'day INT, period Real, nswprice Real, nswdemand Real, vicprice Real,'+
                                   'vicdemand Real, transfer Real, class TEXT)')
                                
                                   

#Load the csv file into csv reader
csvfile = open('electricity-normalized.csv')
creader = csv.reader(csvfile, delimiter=',', quotechar='|')

#Iterate through the csv reader, inserting values into the database
for i in creader:
 

#Values are inserted into appropriate columns of the table
    c.execute(
                """
                INSERT INTO electricity
                    VALUES(?,?,?,?,?,?,?,?,?)
                """, i
                )
            
#close the csv file, close the connection and commit changes
csvfile.close()
conn.commit()
c.close()
conn.close()
                                   
