import random
from pipmachines.character import *
from pipmachines.display import *
from pipmachines.battlestate import *
from pipmachines.inventory import *
from pipmachines.stats import *

def navigate():

    area = character.location

    if area == 0:
        mapOneIntro()
    elif area == 1:
        a = int(input("You can only go north [1] to Map Two."))
        if a == 1:
            mapTwo()
        else:
            print("That's not an option.")

    elif area == 2:
        b = int(input("You can go north [1] to Map Three or south [2] to Map One."))
        if b == 1:
            mapThree()
        elif b == 2:
            mapOne()
        else:
            print("That's not an option.")

    elif area == 3:
        c = int(input("You can only go south [1] to Map Two."))
        if c == 1:
            mapTwo()
        else:
            print("That's not an option.")

def mapOneIntro():
    character.location = 1
    border()
    print("||   Your pilgrimmage to Pergamum brings you to a dense and petrified forest. The skeletal trees")
    print("||   twist and entangle overhead, and an unsettling fog creeps in around you. It could be that you're")
    print("||   just tired, but you swear you keep seeing the same tortured expressions upon the gnarled bark.")
    border()
    mapOne()

def mapOne():
    print("||   How would you like to proceed, ", character.name, "?")
    character.weapon = "Rusty Shortsword"
    addItem("Rusty Shortsword")
    addItem("Chipped Mace")
    addItem("Shabby Stonebow")
    addItem("Warped Wand")

    option = int(menu())
    border()
    if option == 1:
        print("You search around you!")
        battlestate()
    elif option == 2:
        print("You check your inventory!")
        showInventory()
    elif option == 3:
        print("||   [WEAPON]=[", character.weapon, "]   [ARMOR]=[", character.armor, "]   [TRINKET]=[", character.trinket, "]")
    elif option == 4:
        print("You check your stats!")
        showStats()
    
def mapTwo():
    character.location = 2

def mapThree():
    character.location = 3
