def gissning_svår(kod): #funktion för den svåra nivån på mastermind
    feedback = "" #variabel som visar vad som var rätt/fel plats
    
    while True: #while-loop för inmatningssäkerhet
        gissning = "".join(input("Ange gissning som följd av fyra siffror --> ").split()) #input och tar bort mellanslag
        if gissning.isdigit() == False: #inmatningssäkerhet
            print("Gissa fyra SIFFROR!")
        elif len(gissning) != 4: #inmatningssäkerhet
            print("Gissa FYRA siffror!")
        else:
            break
    
    gissning_lista1 = list(gissning) #sifferlista för "✓"
    gissning_lista2 = gissning_lista1.copy() #lista för att kolla ifall siffran i gissning redan gett en checkmark
    kod_lista = list(kod) #lista för att kolla ifall siffran i kod redan gett en checkmark

    for pos, digit in enumerate(gissning_lista1): #for-loop som kollar varje siffra i gissning_lista1
        if digit == kod[pos]: #kollar ifall digit (en siffra i gissnint_lista1) finns i koden
            feedback += "✓ " #lägger till "✓" i feedback ifall digit fanns i kod på samma plats som i gissning
            gissning_lista2[pos] = None #säger att den siffran på den positionen redan har använts
            kod_lista[pos] = None #säger att den siffran i kod redan har funnits

    for digit in gissning_lista2: #for-loop som kollar varje siffra i gissning_lista2
        if digit is not None and digit in kod_lista: #kollar ifall digit inte är använd och den finns i koden
            feedback += "☐ " #lägger till "☐" i feedback ifall digit fanns i kod
            kod_lista[kod_lista.index(digit)] = None #säger att första positionen för digit har använts

    return gissning, feedback.strip()