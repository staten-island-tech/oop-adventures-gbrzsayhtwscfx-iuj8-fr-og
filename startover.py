import random 
PlayerHP = 100
PlayerDMG = 20


class Enemys:
    def __init__(self, id, name):

        self.id = id
        self.name = name

    def SKnightattack(self):
        PlayerHP = 100
        Attacktyp = [1,2,3,4,5,6,7,8,9,10]
        Attacktyp_ = random.choice(Attacktyp)
        attack = [1,2,3,4,5,6]
        magic = [7,8,9]
        heal = [10]
        if  Attacktyp_ in attack:
        # Attack
            PlayerHP -10
        if  Attacktyp_ in magic:
            #Magic
            PlayerHP - 10
        if Attacktyp in heal:
            print("Attack missed")
    SKnightattack()
            

    def Fight1(self):
        numnpc = [5, 6, 7, 8]
        rnpc = random.choice(numnpc)
        whostart = [1,2,3,4,5]
        whostart_ = random.choice(whostart)
        NPCstart = [1,2,3]
        Playerstart = [4,5]
        if rnpc == 5:
            print("5 Sand Knights have spawned!!! ")
            Choice1 =input("Do you wish to fight or leave? ")
            while Choice1 == "fight":
                if whostart_ in NPCstart:
                    SKnightattack()
                if whostart_ in Playerstart:
                    print("WIP")
                else:
                    break

Fight_ = Enemys("self", "id", "name")
Fight1()
            


""" if numstart == 1:
    print("you make the first move")

#not working on this now


while numstart == 2:
    print("your enemy makes the first move")

    numattack = [1, 2, 3, 4]
    rattack = random.choice(numattack)

    def playerattack():
    if rattack == 1:
        PlayerHp = 100
        PlayerHp_ = PlayerHp - 10
        print("you were punched, 10 HP")
        print(PlayerHp_)
        PlayerAttack = input("choose your attack(1,2,3, or 4").capitalize()
        if PlayerAttack == 1:
            print("You have slashed your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 2:
            print("You punched your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break            
            
        
        if PlayerAttack == 3:
            print("your have shot your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")
        
            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 4:
            print("you have kicked your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

    if rattack == 2:
        PlayerHp = 100
        PlayerHp_ = PlayerHp - 10
        print("You were slashed, minus 10 HP")
        print(PlayerHp_)
        PlayerAttack = input("choose your attack(1,2,3, or 4").capitalize()
        if PlayerAttack == 1:
            print("You have slashed your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 2:
            print("You punched your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break            
            
        
        if PlayerAttack == 3:
            print("your have shot your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break    

        if PlayerAttack == 4:
            print("you have kicked your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break
    if rattack == 3:
        PlayerHp = 100
        PlayerHp_ = PlayerHp - 10
        print("You were shot, minus 10 HP")
        print(PlayerHp_)
        PlayerAttack = input("choose your attack(1,2,3, or 4").capitalize()
        if PlayerAttack == 1:
            print("You have slashed your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 2:
            print("You punched your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break            
            
        
        if PlayerAttack == 3:
            print("your have shot your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 4:
            print("you have kicked your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break
    if rattack == 4:
        PlayerHp = 100
        PlayerHp_ = PlayerHp - 10
        print("You were stabbed, minus 10 HP")
        print(PlayerHp_)
        PlayerAttack = input("choose your attack(1,2,3, or 4").capitalize()
        if PlayerAttack == 1:
            print("You have slashed your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 2:
            print("You punched your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break            
            
        
        if PlayerAttack == 3:
            print("your have shot your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")
            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break

        if PlayerAttack == 4:
            print("you have kicked your enemy")
            npcHP - 10
            print(f"your enemy has {npcHP} HP")

            if npcHP > 0:
                break 
                

            if npcHP <= 0:
                print("you have defeated your enemy")
                break
 """