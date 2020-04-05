import random
from pipmachines.display import *
from pipmachines.character import *
from pipmachines.enemies import *

def wipeSpells():
    file = open("spells.txt", "w")
    file.close()

def showSpells():
    global contents
    print("You have learned the following Spells:")
    file = open("spells.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    length = len(contents)-1
    for i in range(length):
        print(contents[i])

def spellCheck(spellX):
    file = open("spells.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    if spellX in contents:
        print("Found the spell!")
    else:
        print("You don't know a spell like that...")

def addSpell(spellX):
    file = open("spells.txt", ",")
    file.write(str(spellX + ","))
    file.close()

def deleteSpell(spellX):
    file = open("spells.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    file.close()
    if spellX in contents:
        i = contents.index(spellX)
        del contents[i]
        print(contents[i], " was removed from your spells!")
        contents = contents[-1]

        file = open("spell.txt", "w")
        for x in range (0, len(contents)):
            print(contents[x])
            file.write(contents[x] + ",")
        file.close()

def useSpell(ploc, elist, eno):
    border()

    playerLocation = ploc
    enemyNo = eno

    if playerLocation == 1:
        enemyList = [desperate_vagabond, carrion_crow, will_of_the_whisp]
    elif playerLocation == 2:
        enemyList = [cuthroat, rotted_hound, blasphemer]
    elif playerLocation == 3:
        enemyList = [restrained_patient, cadaver_corvid, infant_lifeless]
    elif playerLocation == 4:
        enemyList = [bloodletter, harvester_tick, juvenile_lifeless]
    elif playerLocation == 5:
        enemyList = [inquisitor, rat_king, sable_beast]
    elif playerLocation == 6:
        enemyList = [long_lost_crusader, great_eater, deep_one]

    showSpells()

    border()
    file = open("spells.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    spellX = str(input("||                  Select a Spell:"))
    if spellX == "Invoke Missile" and "Invoke Missile" in contents:
            print("Cast Invoke Missile? It consumes 2 Insight.")
            cast = int(input("[1]=[Cast]     [2]=[Cancel]"))
            if cast == 1:
                if character.insight >= 2:
                    spellInvokeMissile()
                else:
                    print("You don't have the insight to cast this spell.")
            elif cast == 2:
                print("Now what?")
    elif spellX == "Immolate" and "Immolate" in contents:
            print("Cast Immolate? It consumes 4 Insight.")
            cast = int(input("[1]=[Cast]     [2]=[Cancel]"))
            if cast == 1:
                if character.insight >= 4:
                    spellImmolate()
                else:
                    print("You don't have the insight to cast this spell.")
            elif cast == 2:
                print("Now what?")
    elif spellX == "Candlelight" and "Candlelight" in contents:
        print("Cast Candlelight? It consumes 4 Insight.")
        cast = int(input("[1]=[Cast]     [2]=[Cancel]"))
        if cast == 1:
            if character.insight >= 4:
                spellCandlelight()
            else:
                print("You don't have the insight to cast this spell.")
        elif cast == 2:
            print("Now what?")
    elif spellX == "Sunlight" and "Sunlight" in contents:
        print("Cast Sunlight? It consumes 8 Insight.")
        cast = int(input("[1]=[Cast]     [2]=[Cancel]"))
        if cast == 1:
            if character.insight >= 8:
                spellSunlight()
            else:
                print("You don't have the insight to cast this spell.")
        elif cast == 2:
            print("Now what?")

    def enemyCalc(pain):
        newHealth = enemyList[enemyNo].tempHealth - pain
        enemyList[enemyNo].tempHealth = newHealth


    def spellInvokeMissile():
        character.insight = character.insight - 2
        print("Your hand crackles with energy, and with the direction of an outstretched finger, you send a javelin of light at your target!")
        print("The shrieking bolt crashes into your target.")
        rollA = random.randint(1, 3)
        intMod = character.intelligence / 2
        baseDamage = character.mAttackMod * intMod
        damageX = baseDamage + rollA
        rollB = random.randint(1, 3)
        block = enemyList[enemyNo].wisdom + rollB
        damage = damageX - block
        enemyCalc(damage)

    def spellImmolate():
        character.insight = character.insight - 4
        print("You palm glows white-hot as you focus on igniting your target.")
        print("Your foe spontaneously combusts!")
        rollA = random.randint(1, 3)
        intMod = character.intelligence / 2
        baseDamage = intMod * rollA
        damageX = baseDamage + character.mAttackMod
        rollB = random.randint(1, 3)
        block = enemyList[enemyNo].wisdom + rollB
        damage = damageX - block
        enemyCalc(damage)

    def spellCandlelight():
        character.insight = character.insight - 4
        print("A warm and soothing light emits from your hand.")
        rollA = random.randint(1, 3)
        intMod = character.intelligence / 2
        heal = intMod + rollA
        playerHeal = character.health + heal
        character.health = character.health + playerHeal

    def spellSunlight():
        character.insight = character.insight - 8
        print("A warm and soothing light emits from your hand.")
        rollA = random.randint(1, 3)
        intMod = character.intelligence / 2
        heal = intMod * rollA
        playerHeal = character.health + heal
        character.health = character.health + playerHeal