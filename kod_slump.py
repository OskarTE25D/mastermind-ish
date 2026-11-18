import random

def slumpis():
    done = False
    kod = ""
    grad = input("Välj en svårighetsgrad! ('lätt'/'svår') --> ").lower()
    if grad == "lätt":
        while not done:
            num = str(random.randint(1,6))
            if num not in kod:
                kod += num
            if len(kod) == 4:
                done = True
                
    print(kod)
slumpis()    
    #elif grad == "svår":