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
    Rapier_ = ["Aprentice Rapier", "Ironstinger", "Crucible Rapier", "Krystreeza"]
    
    def __init__(self, name, health, damage, rroll, weptype, lightwep):
        super(). __init__(self, name, health, damage, rroll, weptype)
        self.lightwep = lightwep
        
    def ask_weapon(self):
        Ironstinger_ = [1,2,3,4]
        Aprentice_Rapier_ = [5,6,7]
        Crucible_Rapier = [8,9]
        Krystreeza_ = [10]
        weapon_ = input("What is your weapon class?(Light, Medium, Heavy) ").capitalize()
        while weapon_ == "Light":
            Lweapon = input("Dagger, Rapier, or Fist? ").capitalize()
            if Lweapon == "Rapier":
                chance_ = random.choice(self.Chance)
                print(chance_)
                if chance_ in Ironstinger_:
                    self.Stats.append("Weapon: Ironstinger")
                    break
                elif chance_ in Aprentice_Rapier_:
                    self.Stats.append("Weapon : Aprentice Rapier")
                    break
                if  chance_ in Crucible_Rapier:
                    self.Stats.append("Weapon: Crucible Rapier")
                    break
                if chance_ in Krystreeza_:
                    self.Stats.append("Weapon: Krystreeza")
                    break
            if weapon_ == "Medium" and "Heavy":
                break





Player_ = Player("id","name",300,5,0,"weptype")
Player_.name1()
Player_.wep_class
print(Player_.name)
Player1 = Weapon("name","health","damage","rroll","weptype","weapon")
Player1.ask_weapon()
Player_.print_player_stats()


