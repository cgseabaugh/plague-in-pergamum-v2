from pipmachines.display import *
from pipmachines.character import *

def showStats():
    border()
    print("||   [PROFESSION]=[", character.name, "]     [HEALTH]======[", character.maxHealth, "]   [INSIGHT]=[", character.maxInsight, "]")
    print("||   [GOLD]=[", character.gold, "]                [STRENGTH]=====[", character.strength, "]   [VIGOR]===[", character.vigor, "]")
    print("||                               [DEXTERITY]====[", character.dexterity, "]   [REFLEX]==[", character.reflex, "]")
    print("||                               [INTELLIGENCE]=[", character.intelligence, "]   [WISDOM]==[", character.wisdom, "]")
    print("||                                           [WEAPON]==[", character.weapon, "]")
    print("||                                           [ARMOR]===[", character.armor, "]     ")
    print("||                                           [TRINKET]=[", character.trinket, "]")
    print("||                               [PHYS ATTACK]==[", character.pAttackMod, "]   [MAG ATTACK]==[", character.mAttackMod, "]")
    print("||                               [PHYS DEFENSE]=[", character.pDefenseMod, "]   [MAG DEFENSE]=[", character.mDefenseMod, "]")
    border()