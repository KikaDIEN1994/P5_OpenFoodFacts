import mysql.connector 
from peewee import *

conn = mysql.connector.connect(host='127.0.0.1', user='kika2', password='Password123@')
cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS base')
cursor.execute('CREATE DATABASE base')
conn.close()



db = MySQLDatabase('base', host='localhost', port=3306, user='kika2', password='Password123@')
db.connect()

class Product(Model):
   name = CharField()
   nutriscore = CharField()
   stores = CharField()
   url = CharField()

   class Meta:
      database=db
      db_table='Product'



db.create_tables([Product])