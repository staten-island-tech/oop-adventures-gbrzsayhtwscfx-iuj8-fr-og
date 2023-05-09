import random 
PlayerHP = 150
PlayerDMG = 20


class Enemys:
    def __init__(self, id, name):

        self.id = id
        self.name = name




    def SKnighAttack(self):
        NPCAttacktyp = [1,2,3,4,5,6,7,8,9,10]
        NPCAttacktyp_ = random.choice(NPCAttacktyp)
        NPCattack = [1,2,3,4,5,6]
        NPCmagic = [7,8,9]
        NPCheal = [10]
        if  NPCAttacktyp_ in NPCattack:
        # Attack
            attack1 = PlayerHP -100
            print(f"The Sand Knight attacked you. HP: {attack1}")
        if  NPCAttacktyp_ in NPCmagic:
            #Magic
            magic1 = PlayerHP - 15
            print(f"The Sand Knight cast a spell on you. HP: {magic1}")
        if NPCAttacktyp in NPCheal:
            print("Attack missed")

    def PlayerAttack3_SKRM1(self):
        SKRM1_1 = 100
        SKRM1_2 = 100
        SKRM1_3 = 100
        skf1 = PlayerDMG - SKRM1_1
        print(skf1)

            
            
    def SKnightRM1fight1(self):
        print("A")            

"""     def Fight1(self):
        numnpc = [3, 4, 5 ]
        rnpc = random.choice(numnpc)
        whostart = [1,2,3,4,5]
        whostart_ = random.choice(whostart)
        NPCstart = [1,2,3]
        Playerstart = [4,5]
        if rnpc == 3:
            print("3 Sand Knights have spawned!!! ")
            Choice1 =input("Do you wish to fight or leave? ")
            while Choice1 == "fight":
                if whostart_ in NPCstart:
                    self.SKnightattack()
                if whostart_ in Playerstart:
                    self.PlayerAttack3_SKRM1()
                    break
                else:
                    break
 """
Fight_ = Enemys("id", "name")
Fight_.Fight1()
            


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