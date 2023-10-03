
# https://cloud.seenode.com/dashboard/databases#connection

import mysql.connector
import json

with open('credential.json') as f:
  data = json.load(f)

host = data['host']
user = data['username']
password = data['password']

mydb = mysql.connector.connect(
  host = host,
  user = user,
  password = password
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# mysql.connector.errors.DatabaseError
# _mysql_connector.MySQLInterfaceError
