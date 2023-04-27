import random

class Player:
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
    def wep_class(self):
        wep_ = input("What weapon class(Light, Medium, Heavy)? ").capitalize
        self.weptype = wep_


class Light(Player):
    Rapier_ = ["Aprentice Rapier", "Ironstinger", "Crucible Rapier", "Krystreza"]
    def __init__(self, name, health, damage, rroll, weptype, lightwep):
        super(). __init__(self, name, health, damage, rroll, weptype)
        self.lightwep = lightwep
        
    def ask_weapon(self):
        weapon_ = input("What is your weapon class?(Light, Medium, Heavy) ").capitalize()
        while weapon_ == "Light":
            Lweapon = input("Dagger, Rapier, or Fist? ").capitalize()
            if Lweapon == "Rapier":
                lightwep = random.choice(self.Rapier_)
                self.lightwep = lightwep
                print(lightwep)
                break
            if weapon_ == "Medium" and "Heavy":
                break






Player_ = Player("id","name",300,5,0,"weptype")
Player_.name1()
Player_.wep_class
Player1 = Light("name","health","damage","rroll","weptype","weapon")
Player1.ask_weapon()
print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

print(Player_.name)
print(Player1.lightwep)

