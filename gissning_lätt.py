def gissning_lätt(kod):
#☐,✓
    feedback=""
    gissning=input("gissa tal -->")
    for pos, digit in enumerate(gissning):
        if gissning[pos] == kod[pos]:
            feedback+="✓"
        elif digit in kod:
            feedback+="☐"
    return gissning,feedback