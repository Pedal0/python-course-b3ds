import json
from classes.Bibliotheque import add_book, del_book
from classes.Book import statut_book, update_pages

with open('./data/bibliotheque.json', 'r') as json_file:
    df = json.load(json_file)

print("Liste des livres dans la bibliothèque :")
for book in df:
    print(f"ID: {book['id']}, Nom: {book['name']}")

add_or_delete = input("Souhaitez-vous ajouter, supprimer ou consulter un livre ?\n add/del/open: ")

if add_or_delete == "add":
    book_name = input("Entrez le nom du livre à ajouter: ")
    book_length = int(input("Entrez le nombre de pages qu'il contient: "))

    add_book(book_name, book_length)

elif add_or_delete == "del":
    print("Quel livre souhaitez-vous supprimer ?")
    for book in df:
        print(f"ID: {book['id']}, Nom: {book['name']}")

    id = int(input("Entrez l'ID du livre à supprimer: "))
    del_book(id)

elif add_or_delete == "open":
    with open('./data/bibliotheque.json', 'r') as json_file:
        df = json.load(json_file)
    
    print("Quel livre souhaitez-vous lire ou continuer ?")
    for book in df:
        print(f"ID: {book['id']}, Nom: {book['name']}")

    id = int(input("Entrez l'ID du livre à ouvrir: "))
    statut_book(id)

    book_statut = input("Êtes-vous en train de le lire ?\n y/n: ")
    if book_statut.lower() == "y":
        book_page = int(input("À quelle page êtes-vous ? "))
        update_pages(id, book_page)
    else:
        print("Le statut du livre n'a pas été mis à jour.")

