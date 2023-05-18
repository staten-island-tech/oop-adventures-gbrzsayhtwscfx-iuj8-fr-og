
###########
# CLASSES #
###########
import random
r = random
class Warrior:
    def __init__(self, health, attack_1, attack_2, attack_3, heal):
        self.health = health
        self.attack_1 = attack_1
        self.attack_2 = attack_2 
        self.attack_3 = attack_3 
        self.heal = heal 

    def attributes(self):
        # string containing the attributes of the character
        string = "Health: "+ str(self.health) + " Attack 1: "+ str(self.attack_1) + " Attack 2: "+ str(self.attack_2[0]) + "-"+ str(self.attack_2[1])+ " Attack 3: "+ str(self.attack_3[0]) + "-"+ str(self.attack_3[1]) + " Heal:"+ str(self.heal[0]) + "-" + str(self.heal[0])
        return string

    def is_dead(self):
        return self.health <= 0

knight = Warrior(100, 10, (5,15),  (5,25),  (5,10))
mage   = Warrior(50,  15, (10,20), (-5,25), (10,15))
tank = Warrior(150, 5,  (5,10),  (5,15),  (10,20))

while True:
    print("1. Knight: ", knight.attributes())
    print("2. Mage:   ", mage.attributes())
    print("3. Tank: ", tank.attributes())
    player_name = input("What is your character's name? ")
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
        lv_choice = input("Would you like to: 1. Increase max health by 20  2. Increase Healing Factor by 5  3. increase your damage by 5 ")
        if lv_choice == "1":
            health_max += 20
            player.heal
            th = health_max
            return player, health_max
        elif lv_choice == "2":
            player.heal += (5,5)
            player.health = health_max
            return player, health_max
        elif lv_choice == "3":
            player.attack_1 += 5
            player.attack_2 += (5,5)
            player.attack_3 += (5,5)
            player.health = health_max
            return player, health_max
        else:
            print("Please enter in a valid number")
            continue

def difficulty(ai,health_max,level):
    if level == 1:
        return ai
    else:
        ai.health = health_max + 15 * round(0.5 * level + 0.5)
        ai.attack_1 += 5 * round(0.5 * level + 0.5)
        ai.attack_2 += (5 * round(0.5 * level + 0.5),5 * round(0.5 * level + 0.5))
        ai.attack_3 += (5 * round(0.5 * level + 0.5),5 * round(0.5 * level + 0.5))
        ai.heal += (5 * round(0.5 * level + 0.5),5 * round(0.5 * level + 0.5))
        return ai

def randomize_ai(ai):
    ai.health += r.randint(-20,20)
    ai.attack_1 += r.randint(-3,3)
    ai.attack_2 += (r.randint(-3,3),r.randint(-3,3))
    ai.attack_3 += (r.randint(-3,3),r.randint(-3,3))
    ai.heal += (r.randint(-3,3),r.randint(-3,3))
    return ai

#############
# Game Loop #
#############

level = 1
print("\n----------------------- GAME START -----------------------")

while True:
    # Determining AI Class/Stats
    ai_knight = Warrior(100, 10, (5,15),  (5,25),  (5,10))
    ai_mage   = Warrior(50,  15, (10,20), (-5,25), (10,15))
    ai_tank = Warrior(150, 5,  (5,10),  (5,15),  (10,20))
    ai_classes = [ai_knight, ai_mage, ai_tank]


    ai = ai_classes[r.randint(0,2)]
    randomize_ai(ai)
    if ai == ai_knight:
        print("You are fighting a knight with ", ai.health,"HP!")
    elif ai == ai_mage:
        print("You are fighting a mage with ", ai.health,"HP!")
    elif ai == ai_tank:
        print("You are fighting a tank with ", ai.health,"HP!")

    ai_heal_max = ai.health

    ai = difficulty(ai, ai_heal_max, level)

    # Gameplay Loop
    while True:
        # Player Attack
        player_move = input("Would you like to use attack (1), attack (2), attack (3), or heal (4)?  ")
        print("")
        if player_move == "1":
            player_damage = player_class.attack_1
            ai.health = ai.health - player_damage
            print(player_name," did",player_damage,"damage!")
        elif player_move == "2":
            player_damage = r.randint(player_class.attack_2[0],player_class.attack_2[1])
            ai.health = ai.health - player_damage
            print(player_name," did",player_damage,"damage!")
        elif player_move == "3":
            player_damage = r.randint(player_class.attack_3[0],player_class.attack_3[1])
            ai.health = ai.health - player_damage
            print(player_name," did", player_damage, " damage!")
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
            print("Your opponent did ",ai_damage," damage!")
        elif ai_move == 3:
            ai_damage = r.randint(ai.attack_3[0],ai.attack_3[1])
            player_class.health = player_class.health - ai_damage
            print("Your opponent did ", ai_damage," damage!")
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
        print("\nYour health is:", player_class.health,"HP")
        print("Your opponent's health is ", ai.health," HP ")

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
        if points > score:
            hs = open(" highscore.txt "," w ")
            hs.write(str(points))
            hs.write(" \ n ")
            print(" You have the new high score of ",points," !")
            hs.write(player_name)
        else:
            print(" \ nYou finished with ",points," points.")
            print(" The high score is:",score," by ",leader)
        input(" ")
        hs.close()
        break