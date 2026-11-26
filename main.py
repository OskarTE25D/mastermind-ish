#imprtera alla roliga grejor som behövs
from intro import introduktion
from kod_slump import slumpis
from intro import scoreboard
from gissning import gissning_svår

play = True

#print intro via funktion
introduktion()
kod = "1111" #slumpis()
    
#while play==True loop som omringar resten av koden
#kör gissning funktion som tar gissning som input och koden som argument, och returnerar gissningen och feedback,
while play == True:
        # Variabler
        gissning_lista = ["", "", "", "", "", "", "", "", "", "", "", ""]
        feedback_lista = ["    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    "]

        for guess in range(12):
                gissning, feedback = gissning_svår(kod)
                gissning_lista[guess]=gissning
                feedback_lista[guess]=feedback
        
                scoreboard(gissning_lista,feedback_lista)

    #printar tabellen med fin formatering, via funktion.

    #om man inte har rätt, sänks återstående försök
                if gissning == kod:
                    print(f"bra jobbat ig, du gissade rätt på {guess + 1} försök!")
                    break
        else:
                print("Fucking sämst")
                print(f"Rätt kod var: {kod}")
    #fråga om man vill köra igen
        if input("Vill du spela igen? (j/n): ").strip().lower() != "j":
                print('buuuu')
                play = False