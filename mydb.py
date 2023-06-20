import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
    ssl_disabled=True
)

cursorObject = dataBase.cursor()

#Create a database

a = cursorObject.execute("CREATE DATABASE CRM")

print("ALL DONE !")