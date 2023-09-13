import random


print("Kan du gjette hvilket tall jeg tenker på?")

korrekt_svar = random.randint(1,10)

print("Dette er det korrekte svaret:",korrekt_svar) #Dette er kun til bruk under testing, TODO fjern dette.

while True:

    try:

        bruker_svar = int(input("Skriv inn tallet du tror jeg tenker på:"))

        if korrekt_svar == bruker_svar:
            print("Superbra! Du klarte det!")
            break
        elif korrekt_svar == bruker_svar + 1 or korrekt_svar == bruker_svar -1:
            print("Dessverre, du bommet med 1")
        elif bruker_svar == 0:
            print("Takk for at du spilte!")
            break
        else:
            print("Elendig, du må prøve igjen")


    except ValueError:
        print("Du må skrive et tall. Det må være uten desimaler")