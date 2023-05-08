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
        # Light weps

        Messer = [1,2,3]
        Shotel = [5,6,7]
        Serpents_edge = [8,9]
        Shattered_katana = [10]
        Alloyed_Falchion = [4]

        Iron_Spear = [1,2,3,4]
        Ritual_Spear = [5,6,7]
        True_Seraphs_Spear = [8,9]
        Rifle_Spear = [10]

        Mace = [1,2,3,4,5,6,7]
        Sacred_Hammer = [8,9,10]

        Rosens_Peacemaker = [1,2,3,4,5,6]
        Iron_Blunderbuss = [7,8,9]
        # Medium weps

        Avenger = [1,2,3,4,5]
        Zweihander = [6,7]
        Darkalloy_Greatsword = [8,9]
        RailBlade = [10]

        Battleaxe = [1,2,3,4]
        Nightaxe = [5,6,7]
        Alloyed_Canorian_Axe = [8,9]
        Enforcers_Axe = [10]

        Greathammer1 = [1,2,3,4,5]
        Greathammer2 = [6,7,8]
        Greathammer3 = [9]
        Greathammer4 = [10]
        #Heavy weps

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
                if chance_ in Messer:
                    self.Stats.append("Weapon: Messer")
                    break
                if chance_ in Shotel:
                    self.Stats.append("Weapon: Shotel")
                    break
                if chance_ in Serpents_edge:
                    self.Stats.append("Weapon: Serpents Edge")
                    break
                if chance_ in Shattered_katana:
                    self.Stats.append("Weapon: Shattered Katana")
                    break
                if chance_ in Alloyed_Falchion:
                    self.Stats.append("Weapon: Alloyed Falchion")
                    break
            if Mweapon == "Spear":
                if chance_ in Iron_Spear:
                    self.Stats.append("Weapon: Iron Spear")
                    break
                if chance_ in Ritual_Spear:
                    self.Stats.append("Weapon: Ritual Spear")
                    break
                if chance_ in True_Seraphs_Spear:
                    self.Stats.append("Weapon: True Seraphs Spear")
                    break
                if chance_ in Rifle_Spear:
                    self.Stats.append("Weapon: Rifle Spear")
                    break
            if Mweapon == "Club":
                if chance_ in Mace:
                    self.Stats.append("Weapon: Mace")
                    break
                if chance_ in Sacred_Hammer:
                    self.Stats.append("Weapon: Sacred Hammer")
                    break
            if Mweapon == "Rifle":
                if chance_ in Rosens_Peacemaker:
                    self.Stats.append("Weapon: Rosens Peacemaker")
                    break
                if chance_ in Iron_Blunderbuss:
                    self.Stats.append("Weapon: Iron Blunderbuss")
                    break
                
        while weapon_ == "Heavy":
            Hweapon = input("Greatsword, Greataxe, or Greathammer? ").capitalize()
            chance_ = random.choice(self.Chance)
            print(chance_)
            if Hweapon == "Greatsword":
                if chance_ in Avenger:
                    self.Stats.append("Weapon: Avenger")
                    break
                if chance_ in Zweihander:
                    self.Stats.append("Weapon: Greatsword2")
                    break
                if chance_ in Darkalloy_Greatsword:
                    self.Stats.append("Weapon: Greatsword3")
                    break
                if chance_ in RailBlade:
                    self.Stats.append("Weapon: Greatsword4")
                    break
            if Hweapon == "Greataxe":
                if chance_ in Battleaxe:
                    self.Stats.append("Weapon: Battleaxe")
                    break
                if chance_ in Nightaxe:
                    self.Stats.append("Weapon: Greataxe2")
                    break
                if chance_ in Alloyed_Canorian_Axe:
                    self.Stats.append("Weapon: Alloyed Canorian Axe")
                    break
                if chance_ in Enforcers_Axe:
                    self.Stats.append("Weapon: Enforcer Axe")
                    break
            if Hweapon == "Greathammer":
                if chance_ in Greathammer1:
                    self.Stats.append("Weapon: Greathammer1")
                    break
                if chance_ in Greathammer2:
                    self.Stats.append("Weapon: Greathammer2")
                    break
                if chance_ in Greathammer3:
                    self.Stats.append("Weapon: Greathammer")
                    break
                if chance_ in Greathammer4:
                    self.Stats.append("Weapon: Greathammer")
                    break






Player_ = Player("id","name",300,5,0,"weptype")
Player_.name1()
Player_.wep_class
print(Player_.name)
Player1 = Weapon("name","health","damage","rroll","weptype","weapon")
Player1.ask_weapon()
Player_.print_player_stats()


