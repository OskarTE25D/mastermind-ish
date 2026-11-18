import random

def slumpis():
    done = False
    kod = ""
    grad = input("Välj en svårighetsgrad! ('lätt'/'svår') --> ").lower()
    if grad == "lätt":
        while not done:
            num = str(random.randint(1,6))
            print(num)
            if num not in kod:
                if len(kod) == 4:
                    done = True
                kod += num
                
    print(kod)
slumpis()    
    #elif grad == "svår":