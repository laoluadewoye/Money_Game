import basic
import options
import gamble
import gambleExtra

from random import randrange

#Author: Olaoluwa Adeowye
#Date created: 12/13 to 12/14/2021
#Date improved: 12/14 by 5pm

#Where everything gets called in the end
def main():
    #initial values of game
    onHand = 0
    bank = 0
    savings = 0
    day = 1
    week = 0
    
    #start function will give the beginning balance in game
    onHand = basic.start()
    
    #Game will last a year, or however long. Counted in days
    for i in range(365):
        #Clearing the board
        basic.clear()
        
        #Random event
        event = randrange(1, 19)
        if (event == randrange(1, 19)):
            if (bank > 0):  
                randomPending = randomEvent(bank)
                bank += randomPending
        
        #Calling the updated display
        basic.bankDisplay(onHand, bank, savings, day)
        
        #Incrementing days passing
        day += 1
        week+= 1
        if (week == 7):
            print()
            print("A week has passed! Here is 100 dollars.")
            print()
            onHand += 100
            week = 0
        
        #Choosing what to spend day on
        choice = int(input("What option are you doing today: "))
        
        #Choice branch
        if (choice == 1):
            #Pending charge is withdrawn from bank and put in hand
            withdrawPending = options.withdraw(bank)
            bank -= withdrawPending
            onHand += withdrawPending
        elif (choice == 2):
            #Pending charge is taken out of hand and depositied into bank
            depositPending = options.deposit(onHand)
            onHand -= depositPending
            bank += depositPending
        elif (choice == 3):
            #Pending charge is taken out of bank and sent on its way
            transferPending = options.transfer(bank)
            bank -= transferPending
        elif (choice == 4):
            #Pending charge, positive or negative, is added to hand's net balance at end of the day
            potPending = gamble.gamble(onHand, day)
            onHand = onHand + potPending
        elif (choice == 5):
            #Pending charge is deposited to the player at varying degrees
            split = options.workSplit()
            workCheck = work()
            
            #Calculates part of check that goes to bank
            checkPending = workCheck * (split / 100)
            
            #'// 1' is to keep number close to an int even though it is now a double
            bank += (checkPending // 1)
            onHand += ((workCheck - checkPending) // 1)
        elif (choice == 6):
            #Growth when money amount is altered first
            #First creates pending interest charge
            interestPending = options.interest(savings)
            
            #If the supposed net result of transaction is bigger than the current amount of savings...
            #Money is taken out of hand as it is being put into savings account.
            #Amount taken is calculated by subtracting supposed net with actual amount to find the discrepancy added
            if (interestPending > savings):
                onHand = onHand - (interestPending - savings)
                
            #If the supposed net result of transaction is smaller than the current amount of savings...
            #Money is added to hand as it is being drawn out of savings account.
            #Amount taken is calculated by subtracting actual amount with supposed net to find the discrepancy added
            elif(interestPending < savings):
                onHand = onHand + (savings - interestPending)
                
            #If both sides are equal, it is suspected nothing was changed and everything remains the same
            elif(interestPending == savings):
                onHand = onHand + 0
            
            #Pending amount in savings account is now established
            savingsPending = interestPending
            savings = options.interestFormula(savingsPending, day)
        else: 
            #In case someone puts weird number
            print()
            print("Indecisive? Funny? Curious? Whatever it was, you lose a day because of it.")

        if (choice != 6):
            #Passive growth
            savings = options.interestFormula(savings, day)
        
        #For people to actually be able to see results before screen updates
        basic.delay()
    
main()


