from tqdm import tqdm
import model


class Database:
    #  init database product
    def __init__(self, products):
        self.products = products

    def fill_database(self):
        self.fill_product()

    # fill database product and category with get_or_create
    def fill_product(self):
        print("Product inserting ...")
        for product in tqdm(self.products):
            model.Product.get_or_create(
                name=product.name,
                nutriscore=product.nutriscore,
                stores=product.stores,
                url=product.url,
            )
            product_selected = model.Product.select().where(
                model.Product.name == product.name,
                model.Product.nutriscore == product.nutriscore,
                model.Product.url == product.url,
            )
            print(product.name)
            for category in product.categories:
                self.fill_category(category)
                category_selected = model.Category.select().where(
                    model.Category.name_category == category
                )
                self.fill_categorized(product_selected, category_selected)

    def fill_category(self, category):
        model.Category.get_or_create(name_category=category)

    # fill database of categorized
    def fill_categorized(self, product, category):
        if len(product) > 1:
            product = product[0]
        model.Categorized.get_or_create(product_fk=product, category_fk=category)
