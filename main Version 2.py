from os import system, name
import time
import random

#Author: Olaoluwa Adeowye
#Date created: 12/13 to 12/14/2021
#Date improved: 12/14 by 5pm

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
    time.sleep(1)
    print("4 seconds till refresh")
    time.sleep(1)
    print("3 seconds till refresh")
    time.sleep(1)
    print("2 seconds till refresh")
    time.sleep(1)
    print("1 seconds till refresh")
    time.sleep(1)

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
    print(" | Savings = ", num3, "|")
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

#How the withdraw function will work
def withdraw(num):
    print("This option lets you take out money from the bank")
    print()
    draw = int(input("How much many are you taking out: "))
    
    if (belowZero(draw) == True):
        #A catch-22
        if (draw > num):
            print("You don't have that much money and the bank found out.")
            print("You lose a day due to clerical errors.")
            draw = 0
    else:
        print("No numbers under zero.")
        draw = 0
    
    #returns amount drawn from bank for caluclations in main
    return draw

#How the deposit function will work
def deposit(num):
    print("This option lets you keep money safe in the bank")
    print()
    dep = int(input("How much money are you putting away: "))
    
    if (belowZero(dep) == True):
        #A catch-22
        if (dep >= num):
            print("You messed up the bank form, you lose a day due to clerical errors.")
            print("That, or you tried to take all of your money. Bank policy says I can't let you do that.")
            dep = 0
    else:
        print("No numbers under zero.")
        dep = 0
    
    #returns amount deposited into bank for caluclations in main
    return dep

#How the transfer function will work
def transfer(num):
    print("This option lets you give money to someone.")
    print("This can only be done through the bank.")
    send = int(input("How much are you giving? "))
    
    if (send < 0):
        print()
        print("Oh you're TAKING money. Usually I would have a negative check coded for this but....alright I got you, I got you. *wink*")
        if (send < -150):
            print("Although you're being a little greedy. You have to be lowkey about it.")
            print("That's right, they caught you. Gotta pay up now, sorry.")
            send *= (-1.5)
            send = send // 1
            return send
    
    #Another catch-22
    elif (send > num):
        print("Altruism is great and all, but don't give what you don't have please.")
        send = 0
        return send
    
    
    destination = int(input("Is it going to a place, person or organization? (1 for place, 2 for person, 3 for org): "))
    print("What is the name? (if you don't want to, you can say they are anonymous): ")
    name = input()
    
    #Put here for proper grammar for appreciation message
    if (destination == 1):
        print("I am sure that the location of", name, "will appreciate the money transfer.")
    elif (destination == 2):
        print("I am sure that", name, "will appreciate the money transfer.")
    elif (destination == 3):
        print("I am sure that the", name, "will appreciate the money transfer.")
    
    return send

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
        payout = blackjack()
        
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
        payout = random.randrange(1, (365 - time))
        
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
        fighterChoice = int(input("So, are you putting your money on figher 1 or fighter 2? (pick one of the numbers):"))
        
        #Establishing everyone else betting on each side
        fighter1 = random.randrange(1, 24)
        fighter2 = 23 - fighter1
        
        #The total prize pool after everyone bets
        groupPot = random.randrange(13000, 40000)
        
        #Win condition
        fighterWin = random.randrange(1, 3)
        
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
        chance = random.randrange(1, 6)
        print()
        print("You have a", chance, "% chance of getting this!")
        
        #Establishing the chance
        trueChance = random.randrange(1, 101)
        
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

#The actual blackjack game
def blackjack():
    #Starting values
    you = 0
    dealer = 0
    
    #Explaining house rules aka why I am not making a full simulation of BJ at 3 in the morning
    print()
    print("Welcome to blackjack!")
    print("As it is python BJ, we will start from nil.")
    print("House rules are that there will be three rounds. If no one goes over, then the highest one wins.")
    print("Win = pot doubled. Lose = pot lost. Draw = pot returned.")
    print("Now start drawing!")
    
    #Three rounds 
    for i in range(3):
        print()
        print("you =", you)
        print("dealer =", dealer)
        print()
        
        #User choosing what to do
        choiceBJ = int(input("Do you stand or hit? (0 for stand, 1 for hit): "))
        if (choiceBJ == 0):
            print("You decide to stand.")
        elif (choiceBJ == 1):
            print("You decide to hit.")
            card = random.randrange(1,15)
            trueCard = blackjackValue(card)
            you += trueCard
        print()
        
        #Dealer 'choosing' what to do
        dealerdecision = random.randrange(1,4)
        if (dealerdecision == 1):
            print("Dealer decides to stand.")
        elif (dealerdecision > 1):
            print("Dealer decides to hit.")
            card = random.randrange(1,15)
            trueCard = blackjackValue(card)
            dealer += trueCard
        print()
        
        #Instant win conditions
        if (you == 21):
            print("You got a Blackjack, you win!")
            return 1
        elif (you > 21):
            print("You went over before the dealer, you lose.")
            return 2
        elif (dealer == 21):
            print("Dealer got a blackjack, you lost. That's tough...")
            return 2
        elif (dealer > 21):
            print("Dealer went over before you, you win!")
            return 1
    
    #Long-term win conditions
    if (you <= 4):
        print("No. Just no. You know what you did.")
        return 2
    elif (you < 10):
        print("Mmhmm....I don't know about you.")
        return 3
    elif (dealer <= 10):
        print("On the behalf of the house I apologize. Please don't sue.")
        return 1
    elif (you > dealer):
        print("After three long rounds, you unfortunately have more. It was a good game though!")
        return 2
    elif (you < dealer):
        print("After three long rounds, you eeked out less than the house. If I wasn't a program, I would be salty.")
        return 1
    elif (you == dealer):
        print("Well then, wow.")
        print("Like H-how???")
        print("Well, here's your money back I guess.")
        return 3

#Blackjack card drawing    
def blackjackValue(num):
    temp = num
    if (num >= 10):
        print("A", temp, "was drawn")
    elif (num < 10):
        if (num > 14):
            print("A face card was drawn")
            temp = 10
        elif (num == 14):
            temp = int(input("You (or the dealer) drew an Ace! Do you want it to be 1 or 11: "))
    
    return temp

#How 'working a job' works
def work():
    print()
    print("Your begin your day....")
    delay()
    
    #Caluclating dollars per hour
    funds = random.randrange(15, 201)
    
    #Eight hours worth of work
    income = funds * 8
    
    print("You made a cool", income, "dollars today.")
    
    #Snappy one liners?
    if (funds == 200):
        print("Swimming in $$$$$$$$$$$!!!!!! Why not get yourself a bonus?")
        income += (400 // random.randrange(1, 9))
    elif (funds > 190):
        print("Swimming in that $$$$$$")
    elif (funds > 150):
        print("You made more money on your bathroom break than some people do an entire day, and you feel damn good about it!")
    elif (funds > 90):
        print("You're pretty sure you worked at least some form of overtime, but who cares? We have MONEY")
    elif (funds > 60):
        print("Cashing this check was a great, GREAT feeling today.")
    elif (funds > 40):
        print("This was a nice day if you do say so yourself. Hopefully there wasn't overtime involved...")
    elif (funds > 25):
        print("Pretty fine, Pretty alright, pretty good day.")
    else:
        print("Another day, another paycheck...")
    
    return income

#Determining how much money goes to bank and how much goes in pocket
def workSplit():
    print("This option lets you earn some earnest money.")
    
    #0 to 100% split
    num = random.randrange(0, 101)
    
    print("Today, the company decided that", num, "% of the check will go to the bank")
    
    #Returns number to be used in split calculations in main
    return num

#How the savings account will work    
def interest(num):
    temp = 0
    trest = 0
    
    print("This option is a way to save up money.")
    
    #Decision branch
    option = int(input("Do you want to remove or add money to this account? (0 for remove, 1 for add): "))
    if (option == 0):
        temp = int(input("State amount: "))
        if (belowZero(temp) == False):
            print("You accidentally put a dash there. We couldn't process the changes.")
            temp = 0
        trest = num - temp
    elif (option == 1):
        temp = int(input("State amount: "))
        if (belowZero(temp) == False):
            print("You accidentally put a dash there. We couldn't process the changes.")
            temp = 0
        trest = num + temp
    else: 
        #Catch-22
        print("Due to a clerical error, there is no money added or drawn.")
        trest = num
        
    return trest

#Calculating growing amount of money with e    
def interestFormula(num, time):
    #The outcome is a point on an exponetial graph. 
    #The pending savings amount is the coefficient for e.
    #The number of days is used in the exponent part of the graph.
    trueInterest = pow((num * 2.71828), (time * (1 / 360)))
    
    return (num + trueInterest)

#Causing some variation with chance
def randomEvent(num1):
    change = 0
    
    #For labeling purposes
    robbery = "Someone snuck up on you and stole your card from your wallet!"
    storm = "A storm came in and shut down the bank! Your account was altered!"
    donation = "Someone was greatful for one of your transfers and gave you some money back!"
    casino = "The casino sent you some money so you stay one of the customers..."
    
    chance = random.randrange(1, 5)
    
    print()
    if (chance == 1):
        change = random.randrange(1, num1)
        print("Someone snuck up on you and stole your card from your wallet!", change, "dollars was lost.")
        change *= (-1)
    elif (chance == 2):
        change = random.randrange((-(num1 * 0.8)), (num1 * 0.8))
        change = change // 1
        print("A storm came in and shut down the bank! Your account was altered!", change, "dollars was applied to your account.")
    elif (chance == 3):
        change = random.randrange(1, (num1 // 2))
        print("Someone was greatful for one of your transfers and gave you some money back!", change, "dollars was given.")
    elif (chance == 4):
        change = random.randrange(10, 301)
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

#Where everything gets called in the end
def main():
    #initial values of game
    onHand = 0
    bank = 0
    savings = 0
    day = 1
    week = 0
    
    #start function will give the beginning balance in game
    onHand = start()
    
    #Game will last a year, or however long. Counted in days
    for i in range(365):
        #Clearing the board
        clear()
        
        #Random event
        event = random.randrange(1, 19)
        if (event == random.randrange(1, 19)):
            if (bank > 0):  
                randomPending = randomEvent(bank)
                bank += randomPending
        
        #Calling the updated display
        bankDisplay(onHand, bank, savings, day)
        
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
            withdrawPending = withdraw(bank)
            bank -= withdrawPending
            onHand += withdrawPending
        elif (choice == 2):
            #Pending charge is taken out of hand and depositied into bank
            depositPending = deposit(onHand)
            onHand -= depositPending
            bank += depositPending
        elif (choice == 3):
            #Pending charge is taken out of bank and sent on its way
            transferPending = transfer(bank)
            bank -= transferPending
        elif (choice == 4):
            #Pending charge, positive or negative, is added to hand's net balance at end of the day
            potPending = gamble(onHand, day)
            onHand = onHand + potPending
        elif (choice == 5):
            #Pending charge is deposited to the player at varying degrees
            split = workSplit()
            workCheck = work()
            
            #Calculates part of check that goes to bank
            checkPending = workCheck * (split / 100)
            
            #'// 1' is to keep number close to an int even though it is now a double
            bank += (checkPending // 1)
            onHand += ((workCheck - checkPending) // 1)
        elif (choice == 6):
            #Growth when money amount is altered first
            #First creates pending interest charge
            interestPending = interest(savings)
            
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
            savings = interestFormula(savingsPending, day)
        else: 
            #In case someone puts weird number
            print()
            print("Indecisive? Funny? Curious? Whatever it was, you lose a day because of it.")

        if (choice != 6):
            #Passive growth
            savings = interestFormula(savings, day)
        
        #For people to actually be able to see results before screen updates
        delay()
    
main()
