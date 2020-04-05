
import random
from pipmachines.character import *
from pipmachines.display import *
from pipmachines.enemies import *
from pipmachines.spells import *
from pipmachines.inventory import *
from pipmachines.stats import *

def battlestate():
    battle = 1
    if character.location == 1:
        enemyList = [desperate_vagabond, carrion_crow, will_of_the_whisp]
    elif character.location == 2:
        enemyList = [cuthroat, rotted_hound, blasphemer]
    elif character.location == 3:
        enemyList = [restrained_patient, cadaver_corvid, infant_lifeless]
    elif character.location == 4:
        enemyList = [bloodletter, harvester_tick, juvenile_lifeless]
    elif character.location == 5:
        enemyList = [inquisitor, rat_king, sable_beast]
    elif character.location == 6:
        enemyList = [long_lost_crusader, great_eater, deep_one]
    enemyNo = random.randint(0, len(enemyList)) + 1

    playerLocation = character.location
    squad = enemyList
    squadId = enemyNo

    print(enemyList[enemyNo].intro)

    def missCheck():
        miss = False
        rollA = random.randint(1, 6)
        rollB = random.randint(1, 6)
        hitChance = character.accuracy + rollA
        missChance = enemyList[enemyNo].reflex + rollB
        if hitChance >= missChance:
            return miss
        else:
            miss = True
            return miss

    def dodgeCheck():
        dodge = False
        rollA = random.randint(1, 6)
        rollB = random.randint(1, 6)
        hitChance = enemyList[enemyNo].accuracy + rollA
        missChance = character.reflex + rollB
        if hitChance > missChance:
            return dodge
        else:
            dodge = True
            return dodge

    def playerAttack():
        rollA = random.randint(1, 3)
        strMod = character.strength / 2
        baseDamage = character.pAttackMod * strMod
        damageX = baseDamage + rollA
        rollB = random.randint(1, 3)
        block = enemyList[enemyNo].vigor + rollB
        damage = damageX - block
        return damage

    def enemyAttack():
        rollA = random.randint(1, 6)
        if enemyList[enemyNo].strength > enemyList[enemyNo].dexterity and enemyList[enemyNo].strength > enemyList[enemyNo].intelligence:
            print("The enemy performs a strong attack!")
            baseDamage = enemyList[enemyNo].strength + rollA
            damage = baseDamage - character.vigor
            return damage
        elif enemyList[enemyNo].dexterity > enemyList[enemyNo].strength and enemyList[enemyNo].dexterity > enemyList[enemyNo].intelligence:
            print("The enemy performs a swift attack!")
            baseDamage = enemyList[enemyNo].dexterity + rollA
            damage = baseDamage - character.vigor
            return damage
        elif enemyList[enemyNo].intelligence > enemyList[enemyNo].strength and enemyList[enemyNo].intelligence > enemyList[enemyNo].dexterity:
            print("The enemy performs a magical attack!")
            baseDamage = enemyList[enemyNo].intelligence + rollA
            damage = baseDamage - character.wisdom
            return damage
        
    def enemyCalc(pain):
        newHealth = enemyList[enemyNo].tempHealth - pain
        enemyList[enemyNo].tempHealth = newHealth
        print("You struck the ", enemyList[enemyNo].name, " for ", pain, " points of damage!")

    def playerCalc(pain):
        character.health = character.health - pain
        print("You were struck by the ", enemyList[enemyNo].name, " for", pain, " points of damage!")

    def playerTurn():
        healthBar(character.health, enemyList[enemyNo].name, enemyList[enemyNo].tempHealth)
        combatMenu()
        action = int(combatMenu())
        if action == 1:     # attack
            miss = bool(missCheck())
            if miss == False:
                dmg = int(playerAttack())
                enemyCalc(dmg)
            else:
                print("Your attack missed.")
        elif action == 2:     # spell
            useSpell(playerLocation, squad, squadId)

        elif action == 3:     # use item
            showInventory()
            # useInventory()
        elif action == 4:     # see stats
            showStats()
        elif action == 5:     # escape
            escape = random.randint(1, 2)
            if escape == 1:
                print("You successfully escaped!")
                battlestate = 0
            else:
                print("You failed to escape...")

    def enemyTurn():
        healthBar(character.health, enemyList[enemyNo].name, enemyList[enemyNo].tempHealth)
        print("The ", enemyList[enemyNo].name, " attacks!")
        dmg = int(enemyAttack())
        playerCalc(dmg)

    while battle == 1:
        playerTurn()
        enemyTurn()
