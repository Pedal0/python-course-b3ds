import random


coup = 1
difficulty = [10,100,1000]
choose_difficulty = int(input("Difficulté 0: 0 a 10 \n Difficulté 1: 0 a 100 \n Difficulté 2: 0 a 1000:\n")) 
user_number = int(input("Entrez votre nombre:"))
selected_difficulty = difficulty[choose_difficulty]
random_number = random.randint(0,selected_difficulty)

print(random_number)

while user_number != random_number :
    if user_number < random_number :
        print("Trop petit")
        coup += 1
        user_number = int(input("Entrez votre nombre:"))
    elif user_number > random_number : 
        print("Trop grand")
        coup += 1
        user_number = int(input("Entrez votre nombre:"))

print("Le nombre est bien: " + str(random_number))
print("Le nombre de coup jouer est de: " + str(coup))

