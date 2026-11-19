#✓☐
def gissning_svår(kod):
    feedback = ""
    gissning = input("Ange gissning som följd av fyra siffror: ")
    
    for pos, digit in enumerate(gissning):
        if gissning[pos] == kod[pos]:
            feedback += "✓"
        elif digit in kod:
            feedback += "☐"
    return gissning, feedback
print(gissning_svår("1212"))