import random

def slumpis(): #funktion
    done = False
    kod = ""
    grad = input("Välj en svårighetsgrad! ('lätt'/'svår') --> ").lower() #frågar om man vill spela lätta eller svåra versionen
    if grad == "lätt":
        while not done: #medan done = False slumpar ett tal och kollar om talet redan finns i kod-variabeln för att inte ha med samma tal i en kod
            num = str(random.randint(1,6))
            if num not in kod:
                kod += num
            if len(kod) == 4:
                done = True
    elif grad == "svår": #samma sak som lätt men utan tal-kontrollen, svårigheten i svår kommer i gissning_svår.py
        while not done:
            num = str(random.randint(1,6))
            kod += num
            if len(kod) == 4:
                done = True
    return kod, grad #returnerar både koden och svårighetsgraden för att veta vilken av de 2 funktionerna/filerna vi har som ska anropas
