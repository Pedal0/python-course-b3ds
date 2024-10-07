import json
class Bibliotheque:

    def __init__(self, id, name, length):
        self.id = id
        self.name = name
        self.length = length

def add_book(name: str, length:int):
    with open('./data/bibliotheque.json', 'r') as json_file:
        df = json.load(json_file)
    
    max_id = max([item["id"] for item in df], default=0)
    new_id = max_id + 1
    
    new_book = {"id": new_id, "name": name, "length": length}
    
    df.append(new_book)
    
    with open('./data/bibliotheque.json', 'w') as json_file:
        json.dump(df, json_file, indent=4)
        json_file.flush()
    
    print(f"Le livre '{name}' a été ajouté avec l'ID {new_id}.")

def del_book(id:int):
    with open('./data/bibliotheque.json', 'r') as json_file:
        df = json.load(json_file)
    df = [item for item in df if item["id"] != id]
    with open('./data/bibliotheque.json', 'w') as json_file:
        json.dump(df, json_file, indent=4)
        json_file.flush()
    print(json.dumps(df, indent=4))
