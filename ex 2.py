import mysql.connector
myconn=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=myconn.cursor()
mycursor.execute('create database if not exists vvis')
mycursor.execute('use vvis')
mycursor.execute(""" create table if not exists teacher(emp_id int primary key,emp_name varchar(15));""")
myconn.close()
print(" database and table created successfuly")
