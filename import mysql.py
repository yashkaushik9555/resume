import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='Yash955')
print(mydb.connection_id)

my_cursor=mydb.cursor()
my_cursor.execute("create database yash")