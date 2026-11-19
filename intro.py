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
    "Drag" och "Feedback" har värdet "{g_l[drag-1]}" resp. "{f_l[drag-1]}", 
    där drag är nummret som visas åt vänster i print-satsen,
    då borde varje position fyllas av rätt värde och standard värdet i g_l och f_l är (""),
    så om den rundan inte körts än borde det lämnas blankt.
    det borde fungera och då behövs yttligare textformatering 
    för höger/vänster-justering av g_l och f_l värderna
    '''
    
    
    
    print(f'''
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
    
    ''')