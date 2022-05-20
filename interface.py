from peewee import fn
from pymysql import NULL
import model


class Interface:

    def menu(self):
        user_input = None
        while(user_input != "3"):
            print("----------- MENU PRINCIPAL -----------")
            print("\n1) Substituer un produit")
            print("2) Voir les favoris")
            print("3) Quitter")
            user_input = input("\nEntrez votre selection : ")

            while user_input not in ("1", "2", "3"):
                user_input = input("Erreur ! : Entrez votre selection : \n")

            if user_input == "1":
                choice_category = self.select_category()
                choice_product = self.select_product(choice_category)
                substitut = self.get_substitut(choice_product)
                if substitut:
                    print("\nLe substitut trouver est le suivant:", substitut.name)
                    self.save_substitut(choice_product, substitut)
                else:
                    self.print_no_substitut()
            if user_input == "2":
                if choice_product == NULL and substitut == NULL:
                    print("Vous n'avez pas encore de favoris")
                else:
                    self.print_favoris(choice_product, substitut)
            if user_input == "3":
                print("Quitter")

    def select_category(self):
        print("Veuillez choisir entre une categorie de 0 à 4\n")
        categories = model.Category.select().order_by(fn.Rand()).limit(5)
        for index, category in enumerate(categories):
            print(f"{index} : {category.name_category}")
        user_input = input("\nEntrez votre selection : ")
        while user_input not in ("0", "1", "2", "3", "4"):
            user_input = input("Erreur ! : Entrez votre selection : ")
        choice_category = categories[int(user_input)]
        return choice_category

    def select_product(self, choice_category):
        category_products = model.Categorized.select().where(model.Categorized.category_fk == choice_category).limit(5)
        print(f"veuillez choisir entre une produit de 0 à {len(category_products) - 1}\n")
        for index, product in enumerate(category_products):
            print(f"{index} : {product.product_fk.name}")
        user_input = input("\nEntrez votre selection : ")
        while user_input not in [str(i) for i in range(len(category_products))]:
            user_input = input("Erreur ! : Entrez votre selection : ")
        choice_product = category_products[int(user_input)].product_fk
        return choice_product

    def get_substitut(self, choice_product):
        categories = model.Categorized.select().where(model.Categorized.product_fk == choice_product)
        categories_fk = []
        original_product_nutri = choice_product.nutriscore
        substitut = None

        for i in categories:
            categories_fk.append(i.category_fk)
        products = model.Categorized.select().where(model.Categorized.category_fk.in_(categories_fk))

        for product in products:
            if original_product_nutri > product.product_fk.nutriscore:
                substitut = product.product_fk
                break
        return substitut

    def print_no_substitut(self):
        print("\nAucun susbtitut trouvé")
        print("Essayer un nouveau produit\n")

    def save_substitut(self, choice_product, substitut):
        user_input = None
        while user_input not in ("oui", "non"):
            user_input = input("\nSouhaitez vous enregistrer le substitut dans vos favoris? ")
            if user_input == "oui":
                model.Favoris.get_or_create(product_fk=choice_product, product_substitut_fk=substitut)
                print("\nLe substitut a été enregistrer")
                # substitut = product.product_fk
                # choice_product
            elif user_input == "non":
                print("\nLe substitut n'a pas été enregistrer")
            else:
                print("\nRéponse incorrect veuillez répondre par oui ou par non")
        return choice_product, substitut

    def print_favoris(self, choice_product, substitut):
        if choice_product == NULL and substitut == NULL:
            print("Vous n'avez pas de favoris")
        else:
            print("Le produit est", choice_product.name)
            print("\nLe substitut est le suivant : ", substitut.name, "\nNote nutriscore :", substitut.nutriscore, "\nLes boutiques du produit :", substitut.stores, "\nAdresse URL:", substitut.url)
