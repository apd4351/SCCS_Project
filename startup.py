import time
import random

def printStartupSequence() :
    print("Initiating terminal startup sequence...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)

    print("Initializing display drivers...")
    ddTime = (random.randrange(800, 5000)) / 1000
    time.sleep(ddTime)
    print("Display drivers initiated. (" + str(ddTime) + ")\n")

    time.sleep(0.5)
    print("Booting memory caches...")
    bmTime = (random.randrange(3000, 8000)) / 1000
    time.sleep(bmTime)
    print("Memory caches booted. (" + str(bmTime) + ")\n")

    time.sleep(0.5)
    print("Attempting network connection...")
    connection_chance = random.randrange(0, 10)

    if connection_chance >= 8:
        conTimeOne = (random.randrange(500, 2500)) / 1000
        time.sleep(conTimeOne)
        print("Connection successful. (" + str(conTimeOne) + ")")
    else:
        time.sleep(5.0)
        print("Connection timed out. (Unsuccessful attempts: 1)")
        if connection_chance >= 3:
            conTimeTwo = (random.randrange(500, 4500)) / 1000
            time.sleep(conTimeTwo)
            timeTwoTotal = conTimeTwo + 5
            print("Connection successful. (" + str(timeTwoTotal) + ")")
        else:
            time.sleep(5.0)
            print("Connection timed out. (Unsuccessful attempts: 2)")
            conTimeThree = (random.randrange(500, 4500)) / 1000
            time.sleep(conTimeThree)
            timeThreeTotal = conTimeThree + 10
            print("Connection successful. (" + str(timeThreeTotal) + ")")
    print("")
    time.sleep(1.0)
    input("Press [enter] to continue...")


def printLogo():
    print('\n' * 2)
    print("    _.-._")
    print("   / \_/ \ ")
    print("   >-(_)-<")
    print("   \_/ \_/")
    print("     '-'")
    print("  Black Rose")
    print('\n' * 6)