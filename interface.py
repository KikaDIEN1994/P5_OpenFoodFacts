class interface:

    def menu():
            print("1) Substituer un produit")
            print("2) Voir les favoris")
            print("3) Quitter")
            user_input = input("Entrez votre selection : ")

            while user_input not in ("1","2","3"):
                user_input = input("Erreur ! : Entrez votre selection : ")
            if user_input == "1":
                print("veuillez choisir entre une categorie de 1 à 5")
            if user_input == "2":
                print("Vous n'avez pas encore de favoris")
            if user_input == "3":
                print("Quitter")

    def select_category():
        pass
    #propose 5 categories au hasard et doit choisir parmi l'un des 5
    #ensuite, une liste de produit sera proposer en fonction de la catégorie choisi a partir de la table categorized
    menu()