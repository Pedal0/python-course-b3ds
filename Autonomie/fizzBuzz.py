def Fizzbuzz(nb):
    if nb % 3 == 0 and nb % 5 == 0:
        return print("Fizz Buzz")
    elif nb % 3 == 0:
        return print("Fizz")
    elif nb % 5 == 0:
        return print("Buzz")
    else:
        return print(nb)

userNumber = int(input("Entrez un nombre: "))

Fizzbuzz(userNumber)