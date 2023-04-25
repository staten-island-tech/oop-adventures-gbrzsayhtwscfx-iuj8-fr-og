import random
hp = 100 

parry = [1, 2, 3, 4, 5,]
def parry_():
    parry1 = random.choice(parry)
    if parry1 == 5:
        print("You parried")
        print(hp)
    else :
        print("You did not parry")
        print(hp - 5)
parry_()
