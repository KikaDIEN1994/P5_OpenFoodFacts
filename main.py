from venv import create
from downloader import Downloader
from database import Database
from interface import Interface
import mysql.connector
import model


def create_database():

    conn = mysql.connector.connect(host='127.0.0.1', user='kika2', password='Password123@')
    cursor = conn.cursor()
    cursor.execute('DROP DATABASE IF EXISTS base')
    cursor.execute('CREATE DATABASE base')
    conn.close()


if __name__ == '__main__':
    user_input = None
    while user_input not in ("oui", "non"):
        user_input = input("\nVoulez vous mettre à jour votre base de donnée? ")
        if user_input == "oui":
            create_database()
            model.create_tables()
            downloader = Downloader(80,10)
            downloader.download()
            products = downloader.get_product_cleaned()
            database = Database(products)
            database.fill_database()

    interface = Interface()
    interface.menu()
