#funktion för den svåra nivån på mastermind
def gissning_svår(kod):
    feedback = "" #variabel som visar vad som var rätt/fel plats
    
    while True: #loop för inmatningssäkerhet
        gissning = "".join(input("Ange gissning som följd av fyra siffror: ").split())
        if gissning.isdigit() == False or len(gissning) != 4:
            print("Gissa fyra siffor!")
        else:
            break

    gissning_lista1 = list(gissning)
    gissning_lista2 = gissning_lista1.copy()
    kod_lista = list(kod)

    for pos, digit in enumerate(gissning_lista1):
        if digit == kod[pos]:
            feedback += "✓"
            gissning_lista2[pos] = None
            kod_lista[pos] = None

    for digit in gissning_lista2:
        if digit is not None and digit in kod_lista:
            feedback += "☐"
            kod_lista[kod_lista.index(digit)] = None

    return gissning, feedback