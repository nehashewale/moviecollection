import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Neha@3010"
)

cus = mydb.cursor()
cus.execute("CREATE DATABASE ott")
