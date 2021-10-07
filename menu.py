"""
This is the menu code, containing functions and tables relevant to the game
"""
# Libraries
import time

# Files
import status

# Menu Variables
PrevMenu = None
CurrentMenu = None

# Menu Functions
def clearConsole():
    print('\n' * 80)

def printMenu(menuObject):
    clearConsole()
    print(menuObject[0])
    time.sleep(menuObject[1])
    clearConsole()
    print(menuObject[2])
    print("")
    choiceNumber = 1
    optionsTable = []
    for choice in menuObject[3]:
        if choice[0] == "Display":
            print(choice[2],":",choice[1][choice[2]])
        if choice[0] == "SubMenu":
            print("[" + str(choiceNumber) + "] " + choice[1])
            optionsTable.insert(choiceNumber-1,choice)
            choiceNumber += 1
        elif choice[0] == "Boolean" and choice[3] is not None:
            successCounter = 0
            for bi in range(len(choice[3])):
                if choice[3][bi][1] == choice[3][bi][2]:
                    successCounter += 1
            if successCounter == len(choice[3]):
                print("[" + str(choiceNumber) + "] " + choice[1])
                choiceNumber += 1
                optionsTable.insert(choiceNumber-1,choice)
    print("")
    return optionsTable


def initializeMenu(menuObject):
    global CurrentMenu
    global PrevMenu
    PrevMenu = CurrentMenu
    CurrentMenu = menuObject
    optionsTable = printMenu(menuObject)
    choiceValid = False
    invalidAttempts = 0
    while not choiceValid:
        pmi = input().lower().strip()
        isInt = False
        try:
            pmi = int(pmi)
            isInt = True
        except ValueError:
            isInt = False
        if isInt and optionsTable[int(pmi)-1] is None:
            print("The choice you have entered is invalid. Please try again.")
            invalidAttempts += 1
        elif not isInt and pmi != "back":
            print("The choice you have entered is invalid. Please try again.")
            invalidAttempts += 1
        else:
            choiceValid = True
        if invalidAttempts > 2:
            time.sleep(1.0)
            print("Too many invalid entries. Reloading Status Interface...")
            time.sleep(2.5)
            invalidAttempts = 0
            clearConsole()
            printMenu(menuObject)
    time.sleep(0.5)
    if pmi != "back":
        initializeMenu(optionsTable[int(pmi)-1][5])
    elif pmi == "back":
        initializeMenu(PrevMenu)



# Menu Object
subsystemsMenu = [
    "Opening Subsystems Status Interface...",
    1,
    "[Subsystems Status Interface]",
    []
]
for key in status.subsystems:
    ot = [
        "Display",
        status.subsystems,
        key
    ]
    subsystemsMenu[3].insert(len(subsystemsMenu[3]),ot)
subsystemsStatus = [
    "SubMenu",
    "Subsystems Status",
    None,
    None,
    None,
    subsystemsMenu
]
conD1 = [
    "Display",
    status.consumables,
    "Food",
]
consumablesMenu = [
    "Opening Consumables Status Interface...",
    1,
    "[Consumables Status Interface]",
    []
]
for key in status.consumables:
    if type(status.consumables[key]) is int:
        ot = [
            "Display",
            status.consumables,
            key
        ]
        consumablesMenu[3].insert(len(consumablesMenu[3]),ot)
consumableStatus = [
    "SubMenu",
    "Consumables Status",
    None,
    None,
    None,
    consumablesMenu
]

mainMenu = [
    "Opening Status Interface...",
    2,
    "[Carrier Status Interface]",
    [
        consumableStatus,subsystemsStatus
    ],
]

"""choiceSample = [
    "ChoiceType",  # SubMenu,Boolean,FunctionCall
    "ChoiceText",
    ["choice1","c1"],  # Valid Text Entries
    [
        ["BOOLEANTHATMUSTBE",False]
        ["BOOLEANTHATMUSTBE",False]
    ],  # Boolean; Can check if false or true
    [
        # Funciton Reference Here... Somehow
    ]
],  # Function Name, can check multiple booleans and multi functions

menuSample = [
    "OpeningString",
    12345,  # Wait Time
    "MenuTitle",
    [
        choiceSample  # ,choice2,choice3
    ],  # Choices Table
]"""