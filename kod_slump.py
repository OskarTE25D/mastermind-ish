import random

def slumpis(): #funktion
    done = False
    kod = ""
    grad = input("\nVälj en svårighetsgrad! ('lätt'/'svår') --> ").lower() #frågar om man vill spela lätta eller svåra versionen
    if grad == "lätt": #random.sample ger 4 tal mellan 1 till 7 (INTE TILL OCH MED) (random.sample(a, b), k) som en lista
        kod = random.sample(range(1,7), 4)
        kod = "".join(map(str, kod)) #konverterar listan till en sträng genom att först ändra varje iteration till en sträng och sedan sätta ihop dem med join
    elif grad == "svår": #samma sak som lätt men utan tal-kontrollen, svårigheten i svår kommer i gissning_svår.py
        for i in range(4):
            kod += str(random.randint(1,6))
    return kod, grad #returnerar både koden och svårighetsgraden för att veta vilken av de 2 funktionerna/filerna vi har som ska anropas