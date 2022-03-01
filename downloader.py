import requests

from tqdm import tqdm

class Product:
    def __init__(self, name, nutriscore, categories, stores, url):
        self.name = name
        self.nutriscore = nutriscore
        self.categories = categories
        self.stores = stores
        self.url = url
        
class Downloader:
    def __init__(self, number_of_product, number_of_page):
        self.number_of_product = number_of_product
        self.number_of_page = number_of_page

    def download(self):#reunion
        self.products_downloaded = []
        print("Downloding ...")
        for i in tqdm(range(1, self.number_of_page+1)):
            response = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",
            params={'page_size': self.number_of_product,
                    'page': i,
                    'action': 'process',
                    'json': 1})
            data = response.json()
            self.products_downloaded.extend(data["products"])
        #print("--------",len(self.products_downloaded))
        self._cleaner()
    
    def get_product_cleaned(self):
       return self.product_cleaned

    def get_category_list(self, category_string):
        categories = []
        for category in category_string.split(','):
            categories.append(category.lower().strip())
            #print(categories)
        
        return categories
        
    def _cleaner(self):
        self.product_cleaned = []
        for product_downloaded in self.products_downloaded:
            name = product_downloaded ["product_name_fr"].lower()
            nutriscore = product_downloaded["nutriscore_grade"].lower()
            url = product_downloaded["url"]
            stores = product_downloaded["stores"]
            categories = self.get_category_list(product_downloaded["categories"])

            product = Product(name, nutriscore,categories, stores,url )
            self.product_cleaned.append(product)