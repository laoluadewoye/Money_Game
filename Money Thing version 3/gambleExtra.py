from random import randrange

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
            card = randrange(1,15)
            trueCard = blackjackValue(card)
            you += trueCard
        print()
        
        #Dealer 'choosing' what to do
        dealerdecision = randrange(1,4)
        if (dealerdecision == 1):
            print("Dealer decides to stand.")
        elif (dealerdecision > 1):
            print("Dealer decides to hit.")
            card = randrange(1,15)
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