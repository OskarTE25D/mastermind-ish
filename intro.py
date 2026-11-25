def introduktion():
    print('''
    Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.
    Du ska försöka gissa denna kods siffror på max 12 drag.
    Efter respektive gissning så kommer du att få en respons:
    För varje gissad korrekt siffra på korrekt plats i koden: ✓
    För varje gissad korrekt siffra på fel plats i koden: ☐
    För de siffror som inte finns med i koden ges ingen markering.

    Exempel: om den slumpade koden är 2315
    och du gissar 3165
    så blir responsen  ✓☐☐

    Du får välja mellan två svårighetsnivåer:
    Lättare nivå: Alla siffror är garanterat olika
    Svårare nivå: Det kan finnas upprepningar av en eller flera siffror
    ''')

def scoreboard(g_l,f_l):
    #g_l = gissning_lista,f_l = feedback_lista, förkortade variabelnamn för att göra textformateringen trevligare.
    #"cur_drag=gissning_lista.index("")", kommer nog inte behöva använda denna.
    
    
    '''
    hur scoreboard kan funka:
    formatera print-satsen nedan så att varje position under 
    "Drag" och "Feedback" har värdet "{g_l[drag]}" resp. "{f_l[drag]}", 
    där drag är nummret som visas åt vänster i print-satsen,
    då borde varje position fyllas av rätt värde och standard värdet i g_l och f_l är (""),
    så om den rundan inte körts än borde det lämnas blankt.
    det borde fungera och då behövs yttligare textformatering 
    för höger/vänster-justering av g_l och f_l värderna
    '''
    print(f"Drag #{" ":>9}Drag{" ":>11}Feedback{" ":>7}\n{"-"*45}\n\n12{g_l[11]:>17}{f_l[11]:>15}\n\n11{g_l[10]:>17}{f_l[10]:>15}\n\n10{g_l[9]:>17}{f_l[9]:>15}\n\n9{g_l[8]:>18}{f_l[8]:>15}\n\n8{g_l[7]:>18}{f_l[7]:>15}\n\n7{g_l[6]:>18}{f_l[6]:>15}\n\n6{g_l[5]:>18}{f_l[5]:>15}\n\n5{g_l[4]:>18}{f_l[4]:>15}\n\n4{g_l[3]:>18}{f_l[3]:>15}\n\n3{g_l[2]:>18}{f_l[2]:>15}\n\n2{g_l[1]:>18}{f_l[1]:>15}\n\n1{g_l[0]:>18}{f_l[0]:>15}\n\n")

#gammal print nedan (obs tog bort citaterna inuti printen)    
'''
print(f
Drag #   Drag           Feedback
---------------------------------------

12

11

10

9

8

7

6

5

4

3

2

1

)
'''    

   