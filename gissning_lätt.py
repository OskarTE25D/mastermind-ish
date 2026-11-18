def gissning_lätt(kod):
#☐,✓
    pos_lista=["","","",""] 
#pos_lista är en lista där varje index har ett värde(rätt/halvrätt/inget) som motsvarar det kända värdet på den indexen i koden. det kan ses som platsen där feedback variabeln byggs
    gissning=input("gissa tal -->")

    for pos, digit in enumerate(gissning):      #kollar vilka nummer som är helt rätt
        if digit == kod[pos]:
            pos_lista[pos]="✓"
            #feedback+="✓"

    for pos, digit in enumerate(gissning):      #kollar vilka nummer som inte är på rätt plats
        if digit in kod and pos_lista[kod.index(digit)]!="✓":
                pos_lista[kod.index(digit)]="☐"
                #feedback+="☐" 

    feedback=("✓ "*pos_lista.count("✓")+ "☐ "*pos_lista.count("☐")).strip()     #omvandlar listan till feedback
    
    return gissning,feedback