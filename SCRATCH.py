import random

class Player:
    Stats = []
    def __init__(self, id, name, health, damage, rroll, weptype):
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage
        self.rroll = rroll
        self.weptype = weptype
        
    def name1(self):
        name_ = input("What is your name? ")
        self.name = name_
        self.Stats.append(self.name)
    def wep_class(self):
        wep_ = input("What weapon class(Light, Medium, Heavy)? ").capitalize
        self.weptype = wep_
        self.Stats.append(self.weptype)
    def print_player_stats(self):
        print(self.Stats)


class Weapon(Player):
    Chance = [1,2,3,4,5,6,7,8,9,10]

    def __init__(self, name, health, damage, rroll, weptype, lightwep):
        super(). __init__(self, name, health, damage, rroll, weptype)
        self.lightwep = lightwep
        
    def ask_weapon(self):
        Ironstinger_ = [1,2,3,4]
        Aprentice_Rapier_ = [5,6,7]
        Crucible_Rapier = [8,9]
        Krystreza_ = [10]

        Flareblood_Kamas = [1]
        Canor_Fang_ = [2,3,4]
        Nemits_Sickle_ = [5,6,7]
        Tanto = [8,9]
        Krulian_Knife = [10]

        Iron_Cestus = [1,2,3,4,5]
        Legion_Cestus = [6,7,8]
        Flamekeeper_Cestus = [9,10]

        weapon_ = input("What is your weapon class?(Light, Medium, Heavy) ").capitalize()
        while weapon_ == "Light":
            Lweapon = input("Dagger, Rapier, or Fist? ").capitalize()
            chance_ = random.choice(self.Chance)
            print(chance_)
            if Lweapon == "Rapier":
                if chance_ in Ironstinger_:
                    self.Stats.append("Weapon: Ironstinger")
                    break
                elif chance_ in Aprentice_Rapier_:
                    self.Stats.append("Weapon : Aprentice Rapier")
                    break
                if  chance_ in Crucible_Rapier:
                    self.Stats.append("Weapon: Crucible Rapier")
                    break
                if chance_ in Krystreza_:
                    self.Stats.append("Weapon: Krystreza")
                    break
            if Lweapon == "Dagger":
                if chance_ in Canor_Fang_:
                    self.Stats.append("weapon: Canor Fang")
                    break
                if chance_ in Nemits_Sickle_:
                    self.Stats.append("Weapon: Nemits Sickle")
                    break
                if chance_ in Tanto:
                    self.Stats.append("Weapon: Tanto")
                    break
                if chance_ in Krulian_Knife:
                    self.Stats.append("Weapon: Krulian Knife")
                    break
                if chance_ in Flareblood_Kamas:
                    self.Stats.append("Weapon: Flareblood Kamas")
                    break
            if Lweapon == "Fist":
                if chance_ in Iron_Cestus:
                    self.Stats.append("Weapon: Iron Cestus")
                    break
                if chance_ in Legion_Cestus:
                    self.Stats.append("Weapon: Legion Cestus")
                    break
                if chance_ in Flamekeeper_Cestus:
                    self.Stats.append("Weapon: Flamekeeper Cestus")
                    break
            if weapon_ == "Heavy":
                break
        while weapon_ == "Medium":
            Mweapon = input("Sword, Club, Spear or Rifle? ").capitalize()
            chance_ = random.choice(self.Chance)
            print(chance_)
            if Mweapon == "Sword":
                print("sword")





Player_ = Player("id","name",300,5,0,"weptype")
Player_.name1()
Player_.wep_class
print(Player_.name)
Player1 = Weapon("name","health","damage","rroll","weptype","weapon")
Player1.ask_weapon()
Player_.print_player_stats()


