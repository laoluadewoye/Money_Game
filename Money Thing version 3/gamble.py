from random import randrange
from basic import delay, belowZero

import gambleExtra

#Code for the Casino
def gamble(num, time):
    #Casino screen
    print("This option lets you gamble your funds away!")
    horiDiv = " -----------------------------"
    
    print()
    print(" |  Welcome to Python Casino!  |")
    print(horiDiv)
    print(horiDiv)
    print(" |  1. Blackjack               |")
    print(" |  2. Double                  |")
    print(" |  3. Boxing                  |")
    print(" |  4. THE BIG ONE             |")
    print()
    print()
    
    #Choosing from casino catalog
    casChoice = int(input("What option are you doing today: "))
    
    if (casChoice == 1):
        #Referencing and final win condition of Blackjack
        pot = int(input("How much are you betting: "))
        if (belowZero(pot) == False):
            print("Ahhh, nope you can't do that here. We're taking 100 dollars for the entry fee though.")
            pot = (-100)
            return pot
        
        #Catch-22
        if (pot > num):
            print("Come back when you have the money. ;-;")
            pot = 0
            return pot
        
        #Final win-condition value
        payout = gambleExtra.blackjack()
        
        if (payout == 1):
            print("Winner!")
        elif (payout == 3):
            print("Draw!")
            pot = 0
        elif (payout == 2):
            print("Loser!")
            pot = pot * (-1)
        
        #returns amount to be added (or subtracted) from hand in main
        return pot    
    
    elif (casChoice == 2):
        #How Doubling money works 
        
        pot = int(input("How much are you betting: "))
        if (belowZero(pot) == False):
            print("Ahhh, nope you can't do that here. We're taking 100 dollars for the entry fee though.")
            pot = (-100)
            return pot
        
        #As time increases, it is going to lower the range and increase the chance that you get a number under 66 and lose
        payout = randrange(1, (365 - time))
        
        if (payout > 65):
            print("Winner!")
        else:
            print("Loser!")
            pot = pot * (-1)
            
        #returns amount to be added (or subtracted) from hand in main
        return pot
    
    elif (casChoice == 3):
        #The boxing betting mechanism 
        
        share = 0
        
        print("Welcome to the boxing ring!")
        print("In here we are watching world class fighters duke it out!")
        print("Minimum pot is 500 dollars")
        pot = int(input("How much are you betting: "))
        if (belowZero(pot) == False):
            print("Ahhh, nope you can't do that here. We're taking 100 dollars for the entry fee though.")
            pot = (-100)
            return pot
        
        #Establishing minimum betting requirement. There is no time for lesser entries.
        if (pot < 500):
            print("You are insulting the sport with that bet. Insulting! Take that rubbish off to blackjack, hmph!")
            pot = 0
            return pot
        
        
        #Choosing who you're betting on to win
        fighterChoice = int(input("So, are you putting your money on figher 1 or fighter 2? (pick one of the numbers): "))
        
        #Establishing everyone else betting on each side
        fighter1 = randrange(1, 24)
        fighter2 = 23 - fighter1
        
        #The total prize pool after everyone bets
        groupPot = randrange(13000, 40000)
        
        #Win condition
        fighterWin = randrange(1, 3)
        
        #Results are nearly mirrored on each side to display both fighters
        if (fighterChoice == 1):
            if (fighterChoice == fighterWin):
                print("You and", fighter1, "others won the grand pot of", groupPot, "!")
                share = groupPot // (fighter1 + 1)
                print("Your share is $", share)
                pot = share
            else:
                print("Your guy lost :/")
                pot = pot * (-1)
                return pot
                
                
        elif (fighterChoice == 2):
            if (fighterChoice == fighterWin):
                print("You and", fighter2, "others won the grand pot of", groupPot, "!")
                share = groupPot // (fighter2 + 1)
                print("Your share is $", share)
                pot = share
            else:
                print("Your guy lost :/")
                pot = pot * (-1)
                return pot
                
        #returns amount to be added (or subtracted) from hand in main
        return pot
    
    #A very, very stupid idea for someone to choose 
    elif (casChoice == 4):
        print("This is THE BIG ONE!!!")
        print("I'm going to be straight up. You have a 1-5% chance of winning. Yes, the chance CHANGES.")
        print("But depending on how much it is, it will be made worth it!")
        print("Minimum pot is 75% of your onhand cash. If you don't want to do this anymore lowball your betting money.")
        print()
        print("I won't judge.")
        pot = int(input("How much are you betting: "))
        
        #A way out. Please take it
        if (pot < (num * 0.75)):
            print("Smart choice. I'm not joking or being sarcastic, it is fine that you don't want to do this.")
            pot = 0
            return pot
        
        #Displaying your chances
        chance = randrange(1, 6)
        print()
        print("You have a", chance, "% chance of getting this!")
        
        #Establishing the chance
        trueChance = randrange(1, 101)
        
        #Making a pot worthy of such craziness
        outcome = pot * (6 - chance) * 20
        
        #SUSPENSE
        delay()
        
        
        if (trueChance <= chance):
            print("Your outcome is $", outcome, "!!!!")
            print("Say, I'm not supposed to get drunk on the job but, you got some money to spare for some shots? :)")
            pot = outcome
        else:
            print("Your outcome is $0...")
            print("...")
            print("Don't even stress about it, no one wins these things anyways. Here, let me get you a drink on me...")
            pot = pot * (-1)
            
        #Once the catharsis kicks in you can see amount to be subtracted from your hand in main.
        return pot