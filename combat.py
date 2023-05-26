import random
r = random
from list import *
class Warrior:
    def __init__(self, health, attack_1, attack_2, heal):
        self.health = health
        self.attack_1 = attack_1
        self.attack_2 = attack_2 
        self.heal = heal 

    def K_attributes(self):
        # string containing the attributes of the character
        wlist = [ Ironstinger , Aprentice_Rapier_, Crucible_Rapier, Krystreza_, Canor_Fang_, Nemits_Sickle_, Tanto, Krulian_Knife, Flareblood_Kamas, Iron_Cestus, Legion_Cestus, Flamekeeper_Cestus, Messer, Shotel, Serpents_edge, Shattered_katana, Alloyed_Falchion, Iron_Spear, Ritual_Spear, True_Seraphs_Spear, Rifle_Spear, Mace, Sacred_Hammer, Rosens_Peacemaker, Iron_Blunderbuss, Avenger, Zweihander, Darkalloy_Greatsword, RailBlade, Battleaxe, Nightaxe, Alloyed_Canorian_Axe, Enforcers_Axe, Steel_Maul, Great_Maul, Petras_Anchor, Hivelords_Hubris ]
        smash = r.choice(wlist)
        smash + 10
        self.attack_1 = smash
        string = "Health: "+ str(self.health) + " Attack 1: "+ str([self.attack_1]) + " Attack 2: "+ str(self.attack_2[0]) + "-"+ str(self.attack_2[1])+  " Heal:"+ str(self.heal[0]) + "-" + str(self.heal[0])
        return string

    def M_attributes(self):
        # string containing the attributes of the character
        wlist = [ Ironstinger , Aprentice_Rapier_, Crucible_Rapier, Krystreza_, Canor_Fang_, Nemits_Sickle_, Tanto, Krulian_Knife, Flareblood_Kamas, Iron_Cestus, Legion_Cestus, Flamekeeper_Cestus, Messer, Shotel, Serpents_edge, Shattered_katana, Alloyed_Falchion, Iron_Spear, Ritual_Spear, True_Seraphs_Spear, Rifle_Spear, Mace, Sacred_Hammer, Rosens_Peacemaker, Iron_Blunderbuss, Avenger, Zweihander, Darkalloy_Greatsword, RailBlade, Battleaxe, Nightaxe, Alloyed_Canorian_Axe, Enforcers_Axe, Steel_Maul, Great_Maul, Petras_Anchor, Hivelords_Hubris ]
        smash = r.choice(wlist)
        smash - 15
        self.attack_1 = smash
        string = "Health: "+ str(self.health) + " Attack 1: "+ str([self.attack_1]) + " Attack 2: "+ str(self.attack_2[0]) + "-"+ str(self.attack_2[1])+  " Heal:"+ str(self.heal[0]) + "-" + str(self.heal[0])
        return string

    def T_attributes(self):
        # string containing the attributes of the character
        wlist = [ Ironstinger , Aprentice_Rapier_, Crucible_Rapier, Krystreza_, Canor_Fang_, Nemits_Sickle_, Tanto, Krulian_Knife, Flareblood_Kamas, Iron_Cestus, Legion_Cestus, Flamekeeper_Cestus, Messer, Shotel, Serpents_edge, Shattered_katana, Alloyed_Falchion, Iron_Spear, Ritual_Spear, True_Seraphs_Spear, Rifle_Spear, Mace, Sacred_Hammer, Rosens_Peacemaker, Iron_Blunderbuss, Avenger, Zweihander, Darkalloy_Greatsword, RailBlade, Battleaxe, Nightaxe, Alloyed_Canorian_Axe, Enforcers_Axe, Steel_Maul, Great_Maul, Petras_Anchor, Hivelords_Hubris ]
        smash = r.choice(wlist)
        smash + 5
        self.attack_1 = smash
        string = "Health: "+ str(self.health) + " Attack 1: "+ str([self.attack_1]) + " Attack 2: "+ str(self.attack_2[0]) + "-"+ str(self.attack_2[1])+  " Heal:"+ str(self.heal[0]) + "-" + str(self.heal[0])
        return string

    def is_dead(self):
        return self.health <= 0

knight = Warrior(100, 0, (10,20), (15,15))
mage   = Warrior(75,  0, (15,40), (10,10))
tank = Warrior(150, 0,  (5,21), (20,20))

while True:
    player_name = input("What is your character's name? ")
    print(f"Welcome, {player_name}, a trial awaits you. Move foward with your heart, and conquer your enemies. You will be ranked based on your ability to beat enemies that become stronger over time. Good luck, {player_name}!")
    print("1. Knight: ", knight.K_attributes())
    print("2. Mage:   ", mage.M_attributes())
    print("3. Tank: ", tank.T_attributes())
    player_class = input("Select your class: 1, 2, or 3: ")
    if player_class == "1":
        player_class = knight
        print("You have selected the Knight class.")


        break
    elif player_class == "2":
        player_class = mage
        print("You have selected the Mage")
        break
    elif player_class == "3":
        player_class = tank
        print("You have selected the Tank")
        break
    else:
        print("Please select a valid class.")
        continue

player_heal_max = player_class.health

def level_up(player, health_max):
    while True:
        lv_choice = input("Would you like to: 1. Increase max health by 20  2. Increase Healing Factor by 5  3. increase your damage by 5    :    ")
        if lv_choice == "1":
            health_max += 20
            player_class.health = health_max
            return player, health_max
        elif lv_choice == "2":
            player_class.heal += (5,5)
            player_class.health = health_max
            return player_class, health_max
        elif lv_choice == "3":
            player_class.attack_1 += 5
            player_class.attack_2 += (5,5)
            player_class.health = health_max
            return player, health_max
        else:
            print("Please enter in a valid number")
            continue

def difficulty(health_max,level):
    if level == 1:
        return ai
    else:
        ai.health = health_max + 25 * round(0.5 * level + 0.5)
        ai.attack_1 += 20 * round(0.5 * level + 0.5)
        ai.attack_2 += (10 * round(0.5 * level + 0.5),5 * round(0.5 * level + 0.5))
        ai.heal += (10 * round(0.5 * level + 0.5),5 * round(0.5 * level + 0.5))
        return ai

def randomize_ai():
    ai.health += r.randint(-20,20)
    ai.attack_1 += r.randint(-3,3)
    ai.attack_2 += (r.randint(-3,3),r.randint(-3,3))
    ai.heal += (r.randint(-3,3),r.randint(-3,3))
    return ai

level = 1
print("----------------------- GAME START -----------------------")

while True:
    # Determining AI Class/Stats
    ai_knight = Warrior(100, 20, (5,15), (5,10))
    ai_mage   = Warrior(75,  10, (10,40), (10,10))
    ai_tank = Warrior(150, 15,  (15,20), (10,5))
    ai_classes = [ai_knight, ai_mage, ai_tank]


    ai = ai_classes[r.randint(0,2)]
    randomize_ai()
    if ai == ai_knight:
        print("You are fighting a knight with ", ai.health,"HP!")
    elif ai == ai_mage:
        print("You are fighting a mage with ", ai.health,"HP!")
    elif ai == ai_tank:
        print("You are fighting a tank with ", ai.health,"HP!")

    ai_heal_max = ai.health

    ai = difficulty(ai_heal_max, level)

    # Gameplay Loop
    while True:
        # Player Attack
        player_move = input("Would you like to use attack (1), attack (2), or heal (4)?  ")
        print("")
        if player_move == "1":
            player_damage = player_class.attack_1
            ai.health = ai.health - player_damage
            print(player_name," did",player_damage,"damage!")
        elif player_move == "2":
            player_damage = r.randint(player_class.attack_2[0],player_class.attack_2[1])
            ai.health = ai.health - player_damage
            if player_damage >= 21:
                print("CRIT!!!")
            print(player_name," did",player_damage,"damage!")
        elif player_move == "4":
            player_heal = r.randint(player_class.heal[0],player_class.heal[1])
            if player_class.health + player_heal > player_heal_max:
                player_class.health = player_heal_max
            else:
                player_class.health = player_class.health + player_heal
            print(player_name," healed for",player_heal,"HP")
        else:
            print("Please enter in a valid move.")
            continue

        # Detecting Death
        if player_class.is_dead():
            break
        elif ai.is_dead():
            points = player_class.health * level
            level += 1
            print("You have bested your opponent! You Have",points,"points. Now starting level",level)
            player_class, player_heal_max = level_up(player_class,player_heal_max)
            break

        # AI Turn
        if ai.health <= (ai_heal_max/5):
            ai_move = r.choice([1,2,3,4,4,4])
        elif ai.health >= (ai_heal_max*.8):
            ai_move = r.choice([1,2,3,1,2,3,4])
        elif ai.health == ai_heal_max:
            ai_move = r.randint(1,3)
        else:
            ai_move = r.randint(1,4)

        if ai_move == 1:
            ai_damage = ai.attack_1
            player_class.health = player_class.health - ai_damage
            print("Your opponent did",ai_damage,"damage!")
        elif ai_move == 2:
            ai_damage = r.randint(ai.attack_2[0],ai.attack_2[1])
            player_class.health = player_class.health- ai_damage
            if ai_damage >= 21:
                print("CRIT!!!")
            print("Your opponent did ",ai_damage," damage!")
        elif ai_move == 4:
            ai_heal = r.randint(ai.heal[0],ai.heal[1])
            if ai.health + ai_heal > ai_heal_max:
                ai.health = ai_heal_max
            if ai.health < 0:
                print("You DIED")
            else:
                ai.health = ai.health + ai_heal
            print("Your opponent healed for ", ai_heal," HP")

        # Displaying HP  
        print("Your health is:", player_class.health,"HP")
        print("Your opponent's health is ", ai.health," HP ")

        if level >= 5:


        # Detecting Death
            if player_class.is_dead():
                break
        elif ai.health <= 0:
            points = player_class.health * level
            level += 1
            print("You have bested your opponent! You Have",points,"points. Now starting level",level)
            player_class, player_heal_max = level_up(player_class,player_heal_max)
            break

    # Finishing Game, Checking/Updating High Score
    if player_class.health<=0:
        print("L + Bozo + ratio")
        if points <= 30:
            print("E Rank")
        if points <= 50:
            print("D Rank")
        if points <= 70:
            print("C Rank")
        if points <= 90:
            print("B Rank")
        if points <= 100:
            print("A Rank")
        if points > 101:
            print("S Rank")

        if points < 0:
            break
        else:
            print("You finished with ",points," points.")
        input(" ")
        break
