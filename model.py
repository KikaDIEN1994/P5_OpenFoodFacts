from peewee import Model, CharField, ForeignKeyField, MySQLDatabase


# Creation database
db = MySQLDatabase('base', host='localhost', port=3306, user='kika2', password='Password123@')
db.connect()


# Creation model product
class Product(Model):
    name = CharField()
    nutriscore = CharField()
    stores = CharField()
    url = CharField()

    class Meta:
        database = db
        db_table = 'Product'


class Category(Model):
    name_category = CharField()

    class Meta:
        database = db
        db_table = 'Category'


class Categorized(Model):
    product_fk = ForeignKeyField(Product)
    category_fk = ForeignKeyField(Category)

    class Meta:
        database = db
        db_table = 'Categorized'


class Favoris(Model):
    product_fk = ForeignKeyField(Product, related_name="original")
    product_substitut_fk = ForeignKeyField(Product, related_name="substitut")

    class Meta:
        database = db
        db_table = 'Favoris'

def create_tables():
    db.create_tables([Product])
    db.create_tables([Category])
    db.create_tables([Categorized])
    db.create_tables([Favoris])
