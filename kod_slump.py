import random

def slumpis():
    done = False
    kod = ""
    grad = input("Välj en svårighetsgrad! ('lätt'/'svår') --> ").lower()
    if grad == "lätt":
        while done == False:
            if len(kod) == 4:
                done == True
            num = str(random.randint(1,6))
            print(num)
            if num not in kod:
                kod += num
                
    print(kod)
slumpis()    
    #elif grad == "svår":