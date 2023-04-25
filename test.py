
damage = 8
health = 1000
class Player:
    def __init__(self, id, name, health, damage ):
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage


        
v=["Blindseer", "Dawnwalker", "Starkindred", "Contractor", "Visionshaper", "Silentheart", "Oathless", "Linkstrider", "Jetstriker", "Arcwarder"]
Rapier_ = ["Aprentice Rapier", "Ironstinger", "Crucible Rapier", "Krystreza"]
Dagger_ = ["Canor Fang", "Tanto"]

name = input("What is your name? ")
y = input("What is your weapon class?(Light, Medium, Heavy) ").capitalize()
if y == "Light":
    Lweapon = input("Dagger, Rapier, or Fist? ").capitalize()
    if Lweapon == "Rapier":
        Rapier1 = input("What type of Rapier? ").capitalize()
    elif Lweapon == "Dagger":
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
    if Rapier1 in Rapier_:
        if Rapier1 == "Ironstinger":
            Ironstinger = (f"Damage: {damage + 10.8}")
            print (Ironstinger)
        if Rapier1 == "Kyrstreeza":
            Kyrstreeza = (f"Damage: {damage + 24.5}")
            print (Kyrstreeza)   
    if Dagger1 in Dagger_:
        if Dagger1 == "Canor Fang":
            Canor_Fang = (f"Damage: {damage + 15.2}")
            print (Canor_Fang)
        if Dagger1 in Dagger_:
            Tanto = (f"Damage: {damage + 20.5}")
            print (Tanto)
lightdmg_()
def LightStat():
    Lucas=Light( name, health, damage, Rapier_, "Apprentice Rapier", "Flamekeeper Cestus")
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