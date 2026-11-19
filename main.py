#imprtera alla roliga grejor som behövs
from intro import introduktion
from kod_slump import slumpis
from gissning_lätt import gissning_lätt
from gissning_svår import gissning_svår

#variabler
play = True
gissning_lista = ["", "", "", "", "", "", "", "", "", "", "", ""]
feedback_lista = ["", "", "", "", "", "", "", "", "", "", "", ""]

#print intro via funktion
introduktion()
kod, grad = slumpis()
    
#while play==True loop som omringar resten av koden
while play == True:
    if grad == "lätt":
        for guess in range(1,13):
            gissning, feedback = gissning_lätt(kod)
            gissning_lista[guess]=gissning
            feedback_lista[guess]=feedback
            
            print(feedback)
            
    if grad == "svår":
        for guess in range(1,13):
            gissning, feedback = gissning_svår(kod)
            gissning_lista[guess]=gissning
            feedback_lista[guess]=feedback
            
            print(feedback)

#kör kodslump funktionen som frågar om svårighetsgrad och returnerar en fyrsiffrig kod

#kör gissning funktion som tar gissning som input och koden som argument, och returnerar gissningen och feedback,

#printar tabellen med fin formatering, via funktion.

#om man inte har rätt, sänks återstående försök

#fråga om man vill köra igen

#hejdå
