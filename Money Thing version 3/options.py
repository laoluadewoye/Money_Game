from random import randrange
from basic import delay, belowZero

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

#How 'working a job' works
def work():
    print()
    print("Your begin your day....")
    delay()
    
    #Caluclating dollars per hour
    funds = randrange(15, 201)
    
    #Eight hours worth of work
    income = funds * 8
    
    print("You made a cool", income, "dollars today.")
    
    #Snappy one liners?
    if (funds == 200):
        print("Swimming in $$$$$$$$$$$!!!!!! Why not get yourself a bonus?")
        income += (400 // randrange(1, 9))
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
    num = randrange(0, 101)
    
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