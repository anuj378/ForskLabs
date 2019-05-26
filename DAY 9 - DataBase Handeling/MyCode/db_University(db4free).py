# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:19:41 2019

@author: King23
"""

'''
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
'''



#!pip install mysql-connector-python
import mysql.connector 
import pandas as pd
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='anuj378', password='mysql_Anuj378',
                              host='db4free.net', database = 'play_db')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE students;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
#c.execute("DROP Table students;")

# STEP 3
c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")


# STEP 4
c.execute("INSERT INTO students VALUES ('Sylvester',18, 100, 'cse')")
c.execute("INSERT INTO students VALUES ('Ankit',18, 101, 'cse')")
c.execute("INSERT INTO students VALUES ('Anuj',19, 102, 'cse')")
c.execute("INSERT INTO students VALUES ('Anmol',20, 103, 'cse')")
c.execute("INSERT INTO students VALUES ('Anupam',19, 104, 'cse')")
c.execute("INSERT INTO students VALUES ('Vikas',18, 105, 'cse')")
c.execute("INSERT INTO students VALUES ('Yash',16, 106, 'cse')")
c.execute("INSERT INTO students VALUES ('Kaushalya',17, 107, 'cse')")
c.execute("INSERT INTO students VALUES ('Preeti',20, 108, 'cse')")
c.execute("INSERT INTO students VALUES ('Gunjan',18, 109, 'cse')")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM students")


# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM students")


# STEP 6
df =pd.DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]

df
