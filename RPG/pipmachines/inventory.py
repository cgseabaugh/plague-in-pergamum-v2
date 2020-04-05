import random
from pipmachines.display import *
from pipmachines.character import *

def itemCheck(itemX):
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    if itemX in contents:
        print("Found the item!")
    else:
        print("You couldn't find the item...")

def addItem(itemX):
    file = open("inventory.txt", "a")
    file.write(str(itemX + ","))
    file.close()

def useInventory(decisionX, contents, itemX):
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    print("What item would you like to see?")
    decisionX = input("Type an item name: ")
    if "Health Drop" in contents and decisionX == "Health Drop":
        print("What would you like to do with the Health Drop?")
    else:
        print("Oh well!")

def deleteItem(decisionX):
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    file.close()
    if decisionX in contents:
        i = contents.index(decisionX)
        del contents[i]
        print(contents[i], " deleted from your inventory!")
        contents = contents[-1]

        file = open("inventory.txt", "w")
        for x in range (0, len(contents)):
            print(contents[x])
            file.write(contents[x] + ",")
        file.close()

def wipeInventory():
    file = open("inventory.txt", "w")
    file.close()

def useTorch():
    print("You ought to save that for when you need it.")
def examTorch():
    print("||   [TORCH] Provides you with a source of both LIGHT and FIRE.")

def useLockpick():
    print("You ought to save that for when you need it.")
def examLockpick():
    print("||   [LOCKPICK] Necessary for getting into locked chests and through locked doors.")

def useHealthdrop():
    print("||   You used a Health Drop and recovered 5 Health.")
    character.health = character.health + 5
    if character.health > character.maxHealth:
        character.health = character.maxHealth
    deleteItem("Health Drop")
def examHealthdrop():
    print("||   [HEALTH DROP] A dropper of liquid that resotres a small amount of health.")

def useHealthvial():
    print("||   You used a Health Vial and recovered 10 Health.")
    character.health = character.health + 10
    if character.health > character.maxHealth:
        character.health = character.maxHealth
    deleteItem("Health Vial")
def examHealthvial():
    print("||   [HEALTH VIAL] A vial of liquid that restores a moderate amount of health.")

def useHealthsyrum():
    print("||   You used a Health Syrum and recovered 20 Health.")
    character.health = character.health + 20
    if character.health > character.maxHealth:
        character.health = character.maxHealth
    deleteItem("Health Syrum")
def examHealthsyrum():
    print("||   [HEALTH SYRUM] A drink that restores a large amount of health.")

def useHealthelixir():
    print("||   You used a Health Elixir and recovered 30 Health.")
    character.health = character.health + 30
    if character.health > character.maxHealth:
        character.health = character.maxHealth
    deleteItem("Health Elixir")
def examHealthelixir():
    print("||   [HEALTH ELIXIR] A potion that restores a tremendous amount of health.")

def useDropofichor():
    print("||   [1]=[Health] [2]=[Insight] [3]=[Strength] [4]=[Dexterity] [5]=[Intelligence] [6]=[Vigor] [7]=[Reflex] [8]=[Wisdom]")
    level = int(input("||          Select an Attribute to Enhance:"))
    if level == 1:
        character.maxHealth = character.maxHealth + 3
        character.Health = character.maxHealth
        print("||   Your Maximum Health was increased.")
    elif level == 2:
        character.maxInsight = character.maxInsight + 1
        character.Insight = character.maxInsight
        print("||   Your Maximum Insight was increased.")
    elif level == 3:
        character.strength = character.strength + 1
        print("||   Your Strength was increased.")
    elif level == 4:
        character.dexterity = character.dexterity + 1
        print("||   Your Dexterity was increased.")
    elif level == 5:
        character.intelligence = character.intelligence + 1
        print("||   Your Intelligence was increased.")
    elif level == 6:
        character.vigor = character.vigor + 1
        print("||   Your Vigor was increased.")
    elif level == 7:
        character.reflex = character.reflex + 1
        print("||   Your Reflex was increased.")
    elif level == 8:
        character.wisdom = character.wisdom + 1
        print("||   Your Wisdom was increased.")
    deleteItem("Drop of Ichor")
def examDropofichor():
    print("The blood of something cosmic; Ingest it to gain an Attribute Point.")

def useChainhauberk():
    character.armor = "Chain Hauberk"
    print("You put on the Chain Hauberk.")
def examChainhauberk():
    print("Its a chain hauberk.")

def usePaddedjacket():
    character.armor = "Padded Jacket"
    print("You put on the Padded Jacket.")
def examPaddedjacket():
    print("Its a padded jacket.")

def useStudiousgown():
    character.armor = "Studious Gown"
    print("You put on the Studious Gown.")
def examStudiousgown():
    print("It's a studious gown.")

def showInventory():
    global contents
    print("You have the following in your inventory:")
    file = open("inventory.txt","r")
    contents = file.read()
    contents = contents.split(",")
    length = len(contents)-1
    for i in range(length):
        print(contents[i])
    print("||               [1]=[Use]     [2]=[Examine]     [3]=[Back]")
    decisionX = int(input("                                      :"))
    if decisionX == 1:
        decisionY = str(input("||         Select an Item You'd like to Use:"))
        if decisionY == "Torch" and decisionY in contents:
            useTorch()
        elif decisionY == "Lockpick" and decisionY in contents:
            useLockpick()
        elif decisionY == "Health Drop" and decisionY in contents:
            useHealthdrop()
        elif decisionY == "Health Vial" and decisionY in contents:
            useHealthvial()
        elif decisionY == "Health Syrum" and decisionY in contents:
            useHealthsyrum()
        elif decisionY == "Health Elixir" and decisionY in contents:
            useHealthelixir()
        elif decisionY == "Drop of Ichor" and decisionY in contents:
            useDropofichor()
        elif decisionY == "Chain Hauberk" and decisionY in contents:
            useChainhauberk()
        elif decisionY == "Padded Jacket" and decisionY in contents:
            usePaddedjacket()
        elif decisionY == "Studious Gown" and decisionY in contents:
            useStudiousgown()
    elif decisionX == 2:
        decisionY = str(input("||     Select an Item You'd Like to Examine:"))
        if decisionY == "Torch" and decisionY in contents:
            examTorch()
        elif decisionY == "Lockpick" and decisionY in contents:
            examLockpick()
        elif decisionY == "Health Drop" and decisionY in contents:
            examHealthdrop()
        elif decisionY == "Health Vial" and decisionY in contents:
            examHealthvial()
        elif decisionY == "Health Syrum" and decisionY in contents:
            examHealthsyrum()
        elif decisionY == "Health Elixir" and decisionY in contents:
            examHealthelixir()
        elif decisionY == "Drop of Ichor" and decisionY in contents:
            examDropofichor()
        elif decisionY == "Chain Hauberk" and decisionY in contents:
            examChainhauberk()
        elif decisionY == "Padded Jacket" and decisionY in contents:
            examPaddedjacket()
        elif decisionY == "Studious Gown" and decisionY in contents:
            examStudiousgown()
    elif decisionX == 3:
        print("Go back!!!")