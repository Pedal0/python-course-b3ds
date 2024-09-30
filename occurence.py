userNumber = int(input("Entrez un nombre: "))
tableMulti = [userNumber*0,userNumber*1,userNumber*2,userNumber*3,userNumber*4,userNumber*5,userNumber*6,userNumber*7,userNumber*8,userNumber*9,userNumber*10]
for i, table in enumerate(tableMulti) :
    if table % 3 == 0 and i != 0:
        table[i] = table[i + "*"]

print(tableMulti)
