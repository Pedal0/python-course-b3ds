import random
difficulty = [10,100,1000]
chooseDifficulty = int(input("Difficulté 0: 0 a 10 \n Difficulté 1: 0 a 100 \n Difficulté 2: 0 a 1000:\n")) 
userNumber = int(input("Entrez votre nombre:"))
selectedDifficulty = difficulty[chooseDifficulty]
randomNumber = random.randint(0,selectedDifficulty)
coup = 1
print(randomNumber)
while userNumber != randomNumber :
    if userNumber < randomNumber :
        print("Trop petit")
        coup += 1
        userNumber = int(input("Entrez votre nombre:"))
    elif userNumber > randomNumber : 
        print("Trop grand")
        coup += 1
        userNumber = int(input("Entrez votre nombre:"))

print("Le nombre est bien: " + str(randomNumber))
print("Le nombre de coup jouer est de: " + str(coup))

