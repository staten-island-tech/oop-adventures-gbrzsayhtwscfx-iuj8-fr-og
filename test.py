import random
damage = 8
health = 400
rroll_ = 1
class Player:
    def __init__(self, id, name, health, damage ):
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage


        
v=["Blindseer", "Dawnwalker", "Starkindred", "Contractor", "Visionshaper", "Silentheart", "Oathless", "Linkstrider", "Jetstriker", "Arcwarder"]
Rapier_ = ["Apprentice Rapier", "Ironstinger", "Crucible Rapier", "Krystreza"]
Dagger_ = ["Canor Fang", "Tanto"]

name = input("What is your name? ")
y = input("What is your weapon class?(Light, Medium, Heavy) ").capitalize()
while y == "Light":
    Lweapon = input("Dagger, Rapier, or Fist? ").capitalize()
    if Lweapon == "Rapier":
        lightwep = random.choice(Rapier_)
        print(lightwep)
        rroll = input("Do you wish to reroll Rapier? y/n ")
        if rroll == "y".capitalize:
            rroll_ = rroll_ + 1
            print(lightwep)
            if rroll_ == 3:
                print("Max rolls reached(3/3) ")
                break
        if rroll == "n":
            print(f"Rolls used: {rroll_}")
            break
            


    if Lweapon == "Dagger":
        Dagger1 = input("What type of Dagger? ").capitalize()
if y == "Heavy":
    Hweapon = input("Ghammer, Gsword, or Gaxe? ").capitalize()
if y == "Medium":
    Mweapon = input("Sword, Spear, or Rifle? ").capitalize()    
z = input("What oath are you going for? ").capitalize()

class Light(Player):

    def __init__( self, name, health, damage, Rapier, Fist, Dagger):
        super().__init__(self,name,health,damage)
        self.Rapier = Rapier
        self.Dagger = Dagger
        self.Fist = Fist
def lightdmg_():
    if "lightwep" in Rapier_:
        if lightwep == "Ironstinger":
            Ironstinger = (f"Damage: {damage + 10.8}")
            print (Ironstinger)
            print(lightwep)
        if lightwep == "Kyrstreeza":
            Kyrstreeza = (f"Damage: {damage + 24.5}")
            print (Kyrstreeza)  
            print(lightwep) 
        if lightwep == "Crucible Rapier":
            Crucible_Rapier = (f"Damage: {damage + 20.6}")
            print (Crucible_Rapier)
            print(lightwep)
        if lightwep == "Apprentice Rapier":
            Apprentice_Rapier = (f"Damage: {damage + 15.9}")
            print (Apprentice_Rapier)
            print(lightwep)


    if "Dagger1" in Dagger_:
        if Dagger1 == "Canor Fang":
            Canor_Fang = (f"Damage: {damage + 15.2}")
            print (Canor_Fang)
        if Dagger1 in Dagger_:
            Tanto = (f"Damage: {damage + 20.5}")
            print (Tanto)
lightdmg_()

def LightStat():
    Lucas=Light( name, health, damage, Rapier_, "Iron cestus", Dagger_)
    print(f"Name:  {Lucas.name}")
    print(f"Health: {Lucas.health}")
    lightdmg_()
    if z in v:
        print(f"Oath: {z}")
"""     if Lweapon == "Rapier": 
        lightdmg_()
    if Lweapon == "Dagger":
        print(Lucas.Dagger)
        print(f"Damage: {damage + 6}")
    if Lweapon == "Fist":
        print(Lucas.Fist)
        print(f"Damage: {damage + 4}") """

LightStat()