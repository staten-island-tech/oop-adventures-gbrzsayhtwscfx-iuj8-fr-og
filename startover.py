HP = 250



attack = 10

PlayerHp = 100

npcHP = [250 - attack]



import random 
numnpc = [3, 4, 5]
rnpc = random.choice(numnpc)
if rnpc == 3:
    print("3 enemies has spawned")
    Jeff = HP

numstart = [1,2]
numstart = random.choice(numstart)

if numstart == 1:
    print("you make the first move")

# after your choice of attack


if numstart == 2:
    print("your enemy makes the first move")

    numattack = [1, 2, 3, 4]
    rattack = random.choice(numattack)

    if rattack == 1:
        PlayerHp - 10
        print("you were punched, 10 HP")
        print(PlayerHp)
        PlayerAttack = input("choose your attack(1,2,3, or 4").capitalize()
        if PlayerAttack == 1:
            print("You have slashed your enemy")


    if rattack == 2:
        PlayerHp - 10
        print("You were slashed, minus 10 HP")
        print(PlayerHp)
    if rattack == 3:
        PlayerHp - 10
        print("You were shot, minus 10 HP")
        print(PlayerHp)
    if rattack == 4:
        PlayerHp - 10
        print("You were stabbed, minus 10 HP")
        print(PlayerHp)
