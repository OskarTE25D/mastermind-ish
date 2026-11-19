#imprtera alla roliga grejor som behövs
from intro import introduktion
from kod_slump import slumpis
from gissning_lätt import gissning_lätt

#variabler
kod, grad = slumpis()
play = True

#print intro via funktion
introduktion()

#skriv koden för lättare versionen först 
if grad == "lätt":
    for guess in range(13):
        gissning, feedback = gissning_lätt(kod)
        print(feedback)
    
#while play==True loop som omringar resten av koden
#while play == True:

#kör kodslump funktionen som frågar om svårighetsgrad och returnerar en fyrsiffrig kod

#kör gissning funktion som tar gissning som input och koden som argument, och returnerar gissningen och feedback,

#printar tabellen med fin formatering, via funktion.

#om man inte har rätt, sänks återstående försök

#fråga om man vill köra igen

#hejdå
