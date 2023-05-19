
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


""" class Oath:
    def __init__( self, Blindseer, Dawnwalker, Starkindred, Contractor, Visionshaper, Silentheart, Oathless, Linkstrider, Jetstriker, Arcwarder):
        self.Blindseer = Blindseer
        self.Dawnwalker = Dawnwalker
        self.Starkindred = Starkindred
        self.Contractor = Contractor
        self.Visionshaper = Visionshaper
        self.Silentheart = Silentheart
        self.Oathless = Oathless
        self.Linkstrider = Linkstrider
        self.Jetstriker = Jetstriker
        self.Arcwarder = Arcwarder """

""" Lucas = Player("input","input","input")
print(Lucas.health) """

name = input("What is your name? ")
y = input("What is your weapon class?(Light, Medium, Heavy) ").capitalize()
if y == "Light":
    Lweapon = input("Dagger, Rapier, or Fist? ").capitalize()
    if Lweapon == "Rapier":
        Rapier1 = input("What type of Rapier? ")
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
            Ironstinger = (f"Damage: {damage + 5}")
            print (Ironstinger)
        if Rapier1 == "Kyrstreeza":
            Kyrstreeza = (f"Damage: {damage + 5}")
            print (Kyrstreeza)   
lightdmg_()
def LightStat():
    Lucas=Light( name, health, damage, Rapier_, "Apprentice Rapier", "Flamekeeper Cestus")
    print(f"Name:  {Lucas.name}")
    print(f"Health: {Lucas.health}")
    if Lweapon == "Rapier": 
        lightdmg_()
    if Lweapon == "Dagger":
        print(Lucas.Dagger)
        print(f"Damage: {damage + 6}")
    if Lweapon == "Fist":
        print(Lucas.Fist)
        print(f"Damage: {damage + 4}")
    if z in v:
        print(f"Oath: {z}")
LightStat()
class Medium(Player):

    def __init__(self, name, health, Sword, Spear, Rifle):
        super().__init__(self,name,health)
        self.Sword = Sword
        self.Spear = Spear
        self.Rifle = Rifle

class Heavy(Player):
    def __init__(self, name, health, Ghammer, Gsword, Gaxe):
        super().__init__(self,name,health)
        self.Ghammer = Ghammer
        self.Gsword = Gsword
        self.Gaxe = Gaxe







if y == "Heavy":
    Lucas=Heavy( name, "health", damage, "Pale Morning", "Enforcer Greatsword", "Evanspear Handaxe")
    print(Lucas.name)
    print(Lucas.health)
    print(Lucas.damage)
    if Hweapon == "Gaxe":
        print(Lucas.Gaxe)
        
    if Hweapon == "Ghammer":
         print(Lucas.Ghammer)
    if Hweapon == "Gsword":
        print(Lucas.Gsword)
    if z in v:
        print(z)

if y == "Light":  
    LightStat()


if y == "Medium":
    Lucas=Medium( name, "150", "Vigil Longsword", "Irontusk", "Ironblunderbuss")
    print(Lucas.name)
    print(Lucas.health)
    if Mweapon == "Sword":
        print(Lucas.Sword)
    if Mweapon == "Spear":
         print(Lucas.Spear)
    if Mweapon == "Rifle":
        print(Lucas.Rifle)
    if z in v:
        print(z)



