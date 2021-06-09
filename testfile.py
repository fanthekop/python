import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234567890"
)

def my_function():
   print(mydb)

def my_function1():
    print(mydb)