NPC = 


numnpcnames = ["Jeff", "Lucas", "Anthony", "Raymond", "Matthew", "Ethan", "Omar"]
rnumnpcnames = random.choice(numnpcnames)

HP = 250

npcdamage = [HP-attack]

class Jeff(NPC):
    Rapier_ = ["Aprentice Rapier", "Ironstinger", "Crucible Rapier", "Krystreza"]
    def __init__(self, name, health, damage, rroll, weptype, lightwep):
        super(). __init__(self, name, health, damage, rroll, weptype)
        self.lightwep = lightwep
    