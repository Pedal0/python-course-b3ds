import json
class Book:
   def __init__(self, id):
      self.id = id

def statut_book(id:int):
    with open('./data/bibliotheque.json', 'r') as json_file:
        df = json.load(json_file)
    
    for item in df:
        for item in df:
            if item["id"] == id:
                if item.get("statut") != "En cours":
                   item["statut"] = "En cours"
                break
    
    with open('./data/bibliotheque.json', 'w') as json_file:
        json.dump(df, json_file, indent=4)
        json_file.flush()
    
    print(f"Le statut du livre a été mis à jour en 'En cours'.")


def update_pages(id:int, book_page:int):
    with open('./data/bibliotheque.json', 'r') as json_file:
        df = json.load(json_file)
    
    for item in df:
        for item in df:
            if item["id"] == id:
                item["pages"] = book_page
                break
    
    with open('./data/bibliotheque.json', 'w') as json_file:
        json.dump(df, json_file, indent=4)
        json_file.flush()
    
    print(f"Vous avez lu {book_page} pages.")
