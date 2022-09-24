import random
Temperature = random.randint(250,1500)  
if(Temperature > 500 ):
    print("ALARM DETECTED")
    print(Temperature)
else:
    print("EVERYTHING LOOKS GOOD")
    print(Temperature)