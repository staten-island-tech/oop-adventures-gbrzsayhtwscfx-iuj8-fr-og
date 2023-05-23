
import random

        
def weps():
    Chance = [1,2,3,4,5,6,7,8,9,10]
    Stats = []
    Ironstinger_ = [1,2,3,4]
    Aprentice_Rapier_ = [5,6,7]
    Crucible_Rapier = [8,9]
    Krystreza_ = [10]

    Flareblood_Kamas = [1]#16
    Canor_Fang_ = [2,3,4]#11
    Nemits_Sickle_ = [5,6,7]#10
    Tanto = [8,9]#15.5
    Krulian_Knife = [10]#12.5

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

    Steel_Maul = [1,2,3,4,5]
    Great_Maul = [6,7,8]
    Petras_Anchor = [9]
    Hivelords_Hubris = [10]
        #Heavy weps

    chance_ = random.choice(Chance)
    print(chance_)

    if chance_ in Ironstinger_:
        ("Weapon: Quickfang")#12
        player_dmg = 12
         
    elif chance_ in Aprentice_Rapier_:
        Stats.append("Weapon : Aprentice Rapier")#13
        player_dmg = 13
         
    if  chance_ in Crucible_Rapier:
        Stats.append("Weapon: Crucible Rapier")#15
        player_dmg = 15
         
    if chance_ in Krystreza_:
        player_dmg = 15
         

    if chance_ in Canor_Fang_:
        Stats.append("weapon: Canor Fang")#11
        player_dmg = 11
         
       
    if chance_ in Nemits_Sickle_:
        Stats.append("Weapon: Nemits Sickle")#10
        player_dmg = 10
         
        
    if chance_ in Tanto:
        Stats.append("Weapon: Tanto")#15.5
        player_dmg = 15.5
         
        
    if chance_ in Krulian_Knife:
        Stats.append("Weapon: Krulian Knife")#12.5
        player_dmg = 12.5
         
        
    if chance_ in Flareblood_Kamas:
        Stats.append("Weapon: Flareblood Kamas")#16
        player_dmg = 16
         
                    
    if chance_ in Iron_Cestus:
        Stats.append("Weapon: Iron Cestus")#13.5
        player_dmg = 13.5
         
        
    if chance_ in Legion_Cestus:
        Stats.append("Weapon: Legion Cestus")#15
        player_dmg = 15
         
    if chance_ in Flamekeeper_Cestus:
        Stats.append("Weapon: Flamekeeper Cestus")#15.5
        player_dmg = 15.5
         
    if chance_ in Messer:
        Stats.append("Weapon: Messer")#20
        player_dmg = 20
         
                   
    if chance_ in Shotel:
        Stats.append("Weapon: Shotel")#22
        player_dmg = 22
         
        
    if chance_ in Serpents_edge:
        Stats.append("Weapon: Serpents Edge")#22
        player_dmg = 22
         
                    
    if chance_ in Shattered_katana:
        Stats.append("Weapon: Shattered Katana")#20
        player_dmg = 20
         
            
    if chance_ in Alloyed_Falchion:
        Stats.append("Weapon: Alloyed Falchion")#16
        player_dmg = 16
         
                  
    
    if chance_ in Iron_Spear:
        Stats.append("Weapon: Iron Spear")#17
        player_dmg = 17
         
                    
    if chance_ in Ritual_Spear:
        Stats.append("Weapon: Ritual Spear")#19
        player_dmg = 19
         
                    
    if chance_ in True_Seraphs_Spear:
        Stats.append("Weapon: True Seraphs Spear")#18.5
        player_dmg = 18.5
         
                    
    if chance_ in Rifle_Spear:
        Stats.append("Weapon: Rifle Spear")#21
        player_dmg = 21
         

    if chance_ in Mace:
        Stats.append("Weapon: Mace")#20
        player_dmg = 20
         
        
    if chance_ in Sacred_Hammer:
        Stats.append("Weapon: Sacred Hammer")#19.5
        player_dmg = 19.5
         
        
    
    if chance_ in Rosens_Peacemaker:
        Stats.append("Weapon: Rosens Peacemaker")#18
        player_dmg = 18
         
                    
    if chance_ in Iron_Blunderbuss:
        Stats.append("Weapon: Iron Blunderbuss")#20
        player_dmg = 20
         
                    
                
     
    if chance_ in Avenger:
        Stats.append("Weapon: Avenger")#21
        player_dmg = 21
         
        
    if chance_ in Zweihander:  
        Stats.append("Weapon: Zweihander")#22
        player_dmg = 22
         
                    
    if chance_ in Darkalloy_Greatsword:
        Stats.append("Weapon: Darkalloy Greatsword")#26
        player_dmg = 26
         
                    
    if chance_ in RailBlade:
        Stats.append("Weapon: RailBlade")#22
        player_dmg = 22
         
                
            
    if chance_ in Battleaxe:    
        Stats.append("Weapon: Battleaxe")#20
        player_dmg = 20
         
                    
    if chance_ in Nightaxe:
        Stats.append("Weapon: Nightaxe")#22
        player_dmg = 22
         
                    
    if chance_ in Alloyed_Canorian_Axe:
        Stats.append("Weapon: Alloyed Canorian Axe")#24
        player_dmg = 24
         

    if chance_ in Enforcers_Axe:
        Stats.append("Weapon: Enforcer Axe")#26
        player_dmg = 26
         
        
           
    if chance_ in Steel_Maul:
        Stats.append("Weapon: Steel Maul")#22
        player_dmg = 22
         
                    
    if chance_ in Great_Maul:
        Stats.append("Weapon: Great Maul")#25
        player_dmg = 25
         
                    
    if chance_ in Petras_Anchor:
        Stats.append("Weapon: Petra's Anchor")#26
        player_dmg = 26
         
                    
    if chance_ in Hivelords_Hubris:
        Stats.append("Weapon: Hivelord's Hubris")#30
        player_dmg = 30
         
         
    print(Stats)
weps()
            