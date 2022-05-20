import requests
import re
from tqdm import tqdm


class Product:
    def __init__(self, name, nutriscore, categories, stores, url):
        """Initialise all argument that we need to identifie product"""
        self.name = name
        self.nutriscore = nutriscore
        self.categories = categories
        self.stores = stores
        self.url = url


class Downloader:
    def __init__(self, number_of_product, number_of_page):
        """Initialise the number of product and page in main.py"""
        self.number_of_product = number_of_product
        self.number_of_page = number_of_page

    def download(self):
        """Downloading all information that we need from url openfoodfact"""
        self.products_downloaded = []
        print("Downloading ...")
        for i in tqdm(range(1, self.number_of_page + 1)):
            response = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl",
                params={
                    "page_size": self.number_of_product,
                    "page": i,
                    "action": "process",
                    "json": 1,
                },
            )
            data = response.json()
            self.products_downloaded.extend(data["products"])
        self._cleaner()

    def get_product_cleaned(self):
        return self.product_cleaned

    def get_category_list(self, category_string):
        """Cleaned category list, remove space and separat with ','"""
        categories = []
        for category in category_string.split(","):
            categories.append(category.lower().strip())

        return categories

    def _cleaner(self):
        """After downloading all product, we cleaned all information like remove all emoji or make all char lower"""
        self.product_cleaned = []
        for product_downloaded in self.products_downloaded:
            if (
                product_downloaded.get("product_name_fr")
                and product_downloaded.get("nutriscore_grade")
                and product_downloaded.get("url")
                and product_downloaded.get("stores")
                and product_downloaded.get("categories")
            ):
                name = product_downloaded["product_name_fr"].lower()
                nutriscore = product_downloaded["nutriscore_grade"].lower()
                url = product_downloaded["url"]
                stores = product_downloaded["stores"]
                categories = self.get_category_list(product_downloaded["categories"])
                emoji_pattern = re.compile(
                    "["
                    "\U0001F600-\U0001F64F"  # emoticons
                    "\U0001F300-\U0001F5FF"  # symbols & pictographs
                    "\U0001F680-\U0001F6FF"  # transport & map symbols
                    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                    "\U00002702-\U000027B0"
                    "\U000024C2-\U0001F251"
                    "\U0001f926-\U0001f937"
                    "\U00010000-\U0010ffff"
                    "\u200d"
                    "\u2640-\u2642"
                    "\u2600-\u2B55"
                    "\u23cf"
                    "\u23e9"
                    "\u231a"
                    "\u3030"
                    "\ufe0f"
                    "]+",
                    flags=re.UNICODE,
                )
                name = emoji_pattern.sub(r"", name)
                product = Product(name, nutriscore, categories, stores, url)
                self.product_cleaned.append(product)
