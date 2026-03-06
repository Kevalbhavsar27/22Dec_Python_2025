import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="22dec_python"
)

cursor = con.cursor()
# cursor.execute("create database 22dec_python")

