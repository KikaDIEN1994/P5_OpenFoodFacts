from downloader import Downloader
from database import Database

if __name__ == '__main__':
    downloader = Downloader(1,1)
    downloader.download()
    products = downloader.get_product_cleaned()
    database = Database(products)
    database.fill_database()
