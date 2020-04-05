import random
import time
from pprint import pprint
from pipmachines.display import *

class character:
    def __init__ (self, name, mhp, hp, mns, ns, str, dex, int, vig, ref, wis, acc, patkMod, matkMod, pdefMod, mdefMod, wep, trnk, arm, xs, gd, loc, prog):
        self.name = name
        self.maxHealth
        self.health = hp
        self.maxInsight
        self.insight = ns
        self.strength = str
        self.dexterity = dex
        self.intelligence = int
        self.vigor = vig
        self.reflex = ref
        self.wisdom = wis
        self.accuracy = acc
        self.pAttackMod = patkMod
        self.mAttackMod = matkMod
        self.pDefenseMod = pdefMod
        self.mDefenseMod = mdefMod
        self.weapon = wep
        self.trinket = trnk
        self.armor = arm
        self.accessory = xs
        self.gold = gd
        self.location = loc
        self.progress = prog

        def getName(self):
            return self.name
        def getHealth(self):
            return self.health
        def getInsight(self):
            return self.insight
        def getStrength(self):
            return self.strength
        def getDexterity(self):
            return self.dexterity
        def getIntelligence(self):
            return self.intelligence
        def getVigor(self):
            return self.vigor
        def getReflex(self):
            return self.reflex
        def getWisdom(self):
            return self.wisdom
        def getAccuracy(self):
            return self.accuracy
        def getPAtkMod(self):
            return self.pAttackMod
        def getMAtkMod(self):
            return self.mAttackMod
        def getPDefMod(self):
            return self.pDefenseMod
        def getMDefMod(self):
            return self.mDefenseMod
        def getWeapon(self):
            return self.weapon
        def getTrinket(self):
            return self.trinket
        def getArmor(self):
            return self.armor
        def getGold(self):
            return self.gold
        def getInventory(self):
            return self.inventory
        def getLocation(self):
            return self.location
        def getProgress(self):
            return self.progress
    
        def setName(self, newName):
            self.name = newName
        def setHealth(self, newHealth):
            self.health = newHealth
        def setInsight(self, newInsight):
            self.insight = newInsight
        def setStrength(self, newStrength):
            self.strength = newStrength
        def setDexterity(self, newDexterity):
            self.dexterity = newDexterity
        def setIntelligence(self, newIntelligence):
            self.intelligence = newIntelligence
        def setVigor(self, newVigor):
            self.vigor = newVigor
        def setReflex(self, newReflex):
            self.reflex = newReflex
        def setWisdom(self, newWisdom):
            self.wisdom = newWisdom
        def setAccuracy(self, newAccuracy):
            self.accuracy = newAccuracy
        def setPAtkMod(self, newPAtkMod):
            self.pAttackMod = newPAtkMod
        def setMAtkMod(self, newMAtkMod):
            self.mAttackMod = newMAtkMod
        def setPDefMod(self, newPDefMod):
            self.mDefenseMod = newPDefMod
        def setMDefMof(self, newMDefMod):
            self.mDefenseMod = newMDefMod
        def setWeapon(self, newWeapon):
            self.weapon = newWeapon
        def setTrinket(self, newTrinket):
            self.trinket = newTrinket
        def setArmor(self, newArmor):
            self.armor = newArmor
        def setGold(self, newGold):
            self.gold = newGold
        def setInventory(self, newInventory):
            self.inventory = newInventory
        def setLocation(self, newLocation):
            self.location = newLocation
        def setProgress(self, newProgress):
            self.progress = newProgress

        def addPAM():
            while self.weapon == "Chipped Hatchet":
                self.pAttackMod = self.pAttackMod + 5
                self.reflex = self.reflex - 1
            while self.weapon == "Rusted Shortsword":
                self.pAttackMod = self.pAttackMod + 3
                self.pDefenseMod = self.pDefenseMod + 1
            while self.weapon == "Shabby Stonebow":
                self.pAttackMod = self.pAttackMod + 2
                self.reflex = self.reflex + 2
            while self.weapon == "Warped Wand":
                self.pAttackMod = self.pAttackMod + 1
                self.mAttackMod = self.mAttackMod + 3
                self.maxInsight = self.maxInsight + 2

def createKnight():
    character.name = "Knight"
    character.maxHealth = 20
    character.health = 20
    character.maxInsight = 4
    character.insight = 4
    character.strength = 5
    character.dexterity = 3
    character.intelligence = 1
    character.vigor = 6
    character.reflex = 2
    character.wisdom = 1
    character.accuracy = 10
    character.pAttackMod = 1
    character.mAttackMod = 1
    character.pDefenseMod = 1
    character.mDefenseMod = 1
    character.weapon = None
    character.trinket = None
    character.armor = None
    character.gold = 0
    character.inventory = []
    character.location = 0
    character.progress = 0

def createHunter():
    character.name = "Hunter"
    character.maxHealth = 16
    character.health = 16
    character.maxInsight = 7
    character.insight = 7
    character.strength = 3
    character.dexterity = 5
    character.intelligence = 3
    character.vigor = 2
    character.reflex = 5
    character.wisdom = 2
    character.accuracy = 10
    character.pAttackMod = 1
    character.mAttackMod = 1
    character.pDefenseMod = 1
    character.mDefenseMod = 1
    character.weapon = None
    character.trinket = None
    character.armor = None
    character.gold = 0
    character.location = 0
    character.progress = 0

def createScholar():
    character.name = "Scholar"
    character.maxHealth = 12
    character.health = 12
    character.maxInsight = 10
    character.insight = 10
    character.strength = 1
    character.dexterity = 3
    character.intelligence = 7
    character.vigor = 1
    character.reflex = 2
    character.wisdom = 5
    character.accuracy = 10
    character.pAttackMod = 1
    character.mAttackMod = 1
    character.pDefenseMod = 1
    character.mDefenseMod = 1
    character.weapon = None
    character.trinket = None
    character.armor = None
    character.gold = 0
    character.location = 0
    character.progress = 0

def createCharacter():
    border()
    a = input("|| What were you, before the plague? [1] Knight [2] Hunter [3] Scholar")
    border()
    while a != "1" and a != "2" and a != "3":
        print("|| That's not an option.")
        a = input("|| What were you, before the plague? [1] Knight [2] Hunter [3] Scholar \n")
    if a == "1":
        createKnight()
    elif a == "2":
        createHunter()
    elif a == "3":
        createScholar()
    
    return(character.name, character.health, character.strength, character.dexterity, character.intelligence, character.vigor, character.reflex, character.wisdom)





