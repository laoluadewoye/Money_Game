from os import system, name
from time import sleep
from random import randrange

#Wipes screen to update display
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def delay():
    print()
    print("Processing changes...")
    sleep(1)
    print("4 seconds till refresh")
    sleep(1)
    print("3 seconds till refresh")
    sleep(1)
    print("2 seconds till refresh")
    sleep(1)
    print("1 seconds till refresh")
    sleep(1)

#Display Graphics
def bankDisplay(num1, num2, num3, time):
    horiDiv = " -----------------------------"
    
    print()
    print(" Day:", time)
    print()
    
    print(horiDiv)
    print(" |  Welcome to Python Bank!  |")
    print(horiDiv)
    print(" | On Hand = ", num1, "  |")
    print(horiDiv)
    print(" | Bank Balance = ", num2, "  |")
    print(horiDiv)
    print(" | Savings = ", format(num3, '.2f'), "|")
    print(horiDiv)
    print(" |          Options          |")
    print(horiDiv)
    print(" | 1. Withdraw   2. Deposit  |")
    print(" | 3. Transfer   4. Gamble   |")
    print(" | 5. Work       6. Interest |")
    print(horiDiv)
    print()
    print()

#Starting rules
def rules():
    print("Here are the rules of the game!")
    print("-------------------------------")
    print("1. You either start with a custom amount or 1000 dollars.")
    print("2. You can do a variety of actions. One action lets a day pass.")
    print("3. To do an action, pick the corresponding number.")
    print("4. Every seven days you get a weekly check of either 100 dollars or a custom amount of your choosing.")
    print("5. This is set to last a year. Go big as much possible before the time is up or you stop the program!")
    print("6. Change the code if you want to, I can't control you. It could teach you some python in the process.")
    print("7. Only use integers! If you see any decimals in this game then I made an error.")
    print()
    print()

#Negative check
def belowZero(num):
    if (num < 0):
        return False
    else:
        return True

#Causing some variation with chance
def randomEvent(num1):
    change = 0
    
    #For labeling purposes
    robbery = "Someone snuck up on you and stole your card from your wallet!"
    storm = "A storm came in and shut down the bank! Your account was altered!"
    donation = "Someone was greatful for one of your transfers and gave you some money back!"
    casino = "The casino sent you some money so you stay one of the customers..."
    
    chance = randrange(1, 5)
    
    print()
    if (chance == 1):
        change = randrange(1, num1)
        print("Someone snuck up on you and stole your card from your wallet!", change, "dollars was lost.")
        change *= (-1)
    elif (chance == 2):
        change = randrange((-(num1 * 0.8)), (num1 * 0.8))
        change = change // 1
        print("A storm came in and shut down the bank! Your account was altered!", change, "dollars was applied to your account.")
    elif (chance == 3):
        change = randrange(1, (num1 // 2))
        print("Someone was greatful for one of your transfers and gave you some money back!", change, "dollars was given.")
    elif (chance == 4):
        change = randrange(10, 301)
        print("The casino sent you some money so you stay one of the customers...", change, "dollars was sent.")
        
    return change

#Starts off player with inital amount of money
def start():
    num = 0
    rules()
    startChoice = int(input("What amount do you want to start with? (0 for default, 1 for custom): "))
    if (startChoice == 0):
        num = 1000
    elif (startChoice == 1):
        num = int(input("Enter amount: "))
        if (belowZero(num) == False):
            print()
            print("You can't start out with negative money. You CAN start out with 0 though.")
            print("Have fun waiting for that check!")
            num = 0
    else:
        print("Not even a day in and the wrong value was put. Shame, guess it's game over.")
        quit()
    delay()
    return num