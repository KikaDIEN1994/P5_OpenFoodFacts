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


class Category(Model):
    name_category = CharField()

    class Meta:
        database=db
        db_table='Category'


class Categorized(Model):
    product_fk = ForeignKeyField(Product)
    category_fk = ForeignKeyField(Category)

    class Meta:
        database=db
        db_table = 'Categorized'


class Favoris(Model):
    product_fk = CharField()
    product_subtitut_fk = CharField()

    class Meta:
        database=db
        db_table = 'Favoris'


db.create_tables([Product])
db.create_tables([Category])
db.create_tables([Categorized])
db.create_tables([Favoris])