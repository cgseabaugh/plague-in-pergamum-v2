
def border():
    print("88", "="*80)

def mainMenu():
    border()
    print("||      ####   #     ##       ####   ##    #  #####            #######   ##    #")
    print("||      #  ##  #     # #     #       ##    #  #                   #      # #   #")
    print("||      ####   #     #  #    #  ###  ##    #  ###                 #      #  #  #")
    print("||      ##     #     #####   #    #   ##   #  #                   #      #   # #")
    print("||      ##     ####  #    #   ####     ####   #####            #######   #    ##")
    border()
    print("||   #####   #####  #####     #####       ####    ##   ##    ###    ###   ##   ##      ")
    print("||   ##  ##  ##     ##   #   ##   ###    ## ##    ###  ###    ##    ##    ###  ###     ")
    print("||   ##  ##  ##     ##   #   ##         ##  ##    #### ####   ##    ##    #### ####    ")
    print("||   #####   ####   #####    ##  ####   ##  ##   ##  ###  ##  ##    ##   ##  ###  ##   ")
    print("||   ##      ##     ##  ##   ##     #   ######   ##   #   ##  ##    ##   ##   #   ##   ")
    print("||   ##      ##     ##  ##   ##    ##  ##   ##   ##        ## ##    ##   ##        ##  ")
    print("||   ##      ##     ##   ##   ##  ##   ##   ##  ##         ##  ##  ##   ##         ##  ")
    print("||   ##      #####  ##    ##   ####   ##    ##  ##         ##   ####    ##         ##  ")
    print("||")
    print("||                     C R E A T E D   B Y   C G S E A B A U G H")
    print("||")
    border()
    border()
    print("||")
    print("||                           [1]=[ B E G I N   G A M E ]")
    print("||")
    print("||                               [2]=[ G U I D E S ]")
    print("||")
    print("||")
    mainMenuX = int(input("||                                        :"))
    if mainMenuX == 1:
        newGameIntro()
    elif mainMenuX == 2:
        print("Read the guide!")
    else:
        mainMenu()

def newGameIntro():
    border()
    print("||   You've come to the great city, PERGAMUM, in search of a cure for the ROTTED PLAGUE")
    print("||   It has devastated your homeland, and rumor has it a CURE has been discovered by")
    print("||   the Ministry of Medicine. Pergamum quickly collapsed under the weight of the plague,")
    print("||   and now the cure, if it even exists, remains lost somewhere inside.")
    border()

def menu():
    border()
    print("||     [1]=[Explore]     [2]=[Inventory]     [3]=[Equipment]     [4]=[Stats]     [5]=[Spell List]")
    border()
    a = input("||                     Select an Option:")
    return a

def combatMenu():
    border()
    print("||   [ 1 ]=[ Attack ]   [ 2 ]=[ Spells ]   [ 3 ]=[ Use Item ]   [ 4 ]=[ Stats ]   [ 5 ]=[ Escape ]   ")
    border()
    b = input("||                          Chose an Action:")
    return b

def healthBar(playerHp, enemyName, enemyHp):
    border()
    print("||          [Your Health]=[", playerHp,"]               [", enemyName, "'s Health]=[", enemyHp,"]")
    border()

def inventoryMenu():
    border()
    print("||               [1]=[Use]     [2]=[Examine]     [3]=[Back]")
    border()