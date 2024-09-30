dictionary_name = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Tree",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
user_input = input("Entrez un numero qui sera épellé: ")
for nb in user_input :
    print(dictionary_name.get(nb))