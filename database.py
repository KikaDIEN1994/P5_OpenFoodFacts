from peewee import *
import model

class Database:
   def __init__(self, products):
       self.products = products
       

   def fill_database(self):
      self.fill_product()

   def fill_product(self):
      for product in self.products:
         model.Product.get_or_create(name=product.name, nutriscore=product.nutriscore,
            stores=product.stores, url=product.url)
