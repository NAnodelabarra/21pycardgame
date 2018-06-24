import random

        #salut
for num in range(1,27): print("\n")
print("""
  /$$$$$$    /$$         /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
 /$$__  $$ /$$$$        | $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
|__/  \ $$|_  $$        | $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$| $$  \ $$| $$  \__/| $$ /$$/ 
  /$$$$$$/  | $$        | $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        | $$| $$$$$$$$| $$      | $$$$$/  
 /$$____/   | $$        | $$__  $$| $$      | $$__  $$| $$      | $$  $$   /$$  | $$| $$__  $$| $$      | $$  $$  
| $$        | $$        | $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$  | $$| $$  | $$| $$    $$| $$\  $$ 
| $$$$$$$$ /$$$$$$      | $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
|________/|______/      |_______/ |________/|__/  |__/ \______/ |__/  \__/ \______/ |__/  |__/ \______/ |__/  \__/
""")

        #variables
global play
global score
global cards
global xd
global ask
global xq
global xe
xe = False
xq = 0
xd = False
play = True
score = 0
cards = 5
ask = "Would you like to start?"

        #ins
print("Do you need instructions?")
ins = input()
ins = str(ins)
while ins != "yes" and ins != "no":
       print ("Say yes or no.")
       ins = input()
       ins = str(ins)
if ins == "yes":
       print("""The aim of the 21 Card Game is to get your score to 21 or as close to as possible. \n Number cards have their face value, but Jacks, Kings and Queens are worth 10. \n  Ace can be either 1 or 11 and the player gets to choose the value of the card. \n   You can ask up to 5 cards, if you need to.""")
if ins == "no":
       print("Let's play then...")
#func
def playagain():
    #variables
    global play
    global score
    global cards
    global xd
    global ask
    global xq
    global xe
    xq = 0
    #playagain
    if play == False:
        print ("Would you like to play again?")
        pla = input()
        pla = str(pla)
        while pla != "yes" and pla != "no":
            print ("Say yes or no.")
            pla = input()
            pla = str(pla)
        if pla == "yes":
            print("Ok then...")
            xe = False
            xd = False
            play = True
            score = 0
            cards = 5
            ask = "Would you like to start?"
        if pla == "no":
            print ("Ok, your final score was",score,"and you had",cards,"cards left.")
            play = False
#ingame
while play == True:
        #intro
            if score > 21:
                print ("You passed 21, your final score was",score,"and you had",cards,"cards left.")
                play = False
                playagain()
            if score == 21:
                print("You got exactly 21 with",cards,"cards left")
                play = False
                playagain()
            if cards == 0:
                print ("You got 0 cards left, you final score was",score,".")
                play = False
                playagain()
            if play == True and score <= 21:
                if xd == True:
                    if xq > 1 and xe == True:
                        print ("your score is",score)
                    print ("and you have",cards,"cards left.")
                    ask = "Would you like another card?"
                print (ask)
                ans = input()
                ans = str(ans)
        #Ans

                while ans != "yes" and ans != "no":
                    print ("Say yes or no.")
                    ans = input()
                    ans = str(ans)
                    
                if ans == "yes":
                    num = random.randint(1,13)
                    xe = True
                    xd = True
                    xq = 1 + xq
        #num
                        #K,Q,J
                    if num == 13:
                            print ("You got a King but it's worth 10")
                            num = 10
                            score += num
                            cards -= 1
                    elif num == 12:
                            print ("You got a Queen but it's worth 10")
                            num = 10
                            score += num
                            cards -= 1
                    elif num == 11:
                            print ("You got a Jack but it's worth 10")
                            num = 10
                            score += num
                            cards -= 1
                        #Ace
                    elif num == 1:
                            print ("You got an Ace, would you like it to be worth 1 or 11?")
                            ace = input()
                            while ace != "1" and ace != "11":
                                print ("Answer 1 or 11.")
                                ace = input()
                            ace = int(ace)
                            if ace == 1:
                                score += ace
                                cards -= 1
                                print ("Your Ace is worth 1.")
                            elif ace == 11:
                                score += ace
                                cards -= 1
                                print ("Your Ace is worth 11.")
                            else:
                                while ace != "1" and ace != "11":
                                    print ("Say 1 or 11.")
                                    ace = int(input(), 10)
                        #Others
                    else:
                            print ("You got a",num)
                            score += num
                            cards -= 1
                elif ans == "no":
                    if xq < 1:
                        print ("Ok, you didn't even played.")
                        play = False
                    if xq >= 1 and xe == True:
                        play = False
                        playagain()


#5 hands each. Aim of the 21 Card Game is to get 21 or as close to as possible.
# Number cards have their face value, jacks, kings and queens are worth 10.
# Ace can be either 1 or 11 and the player who holds the ace gets to choose the value of the card.

"""
if play == False:
    print ("Would you like to play again?")
    pla = input()
    pla = str(pla)
    while pla != "yes" and pla != "no":
        print ("Say yes or no.")
        pla = input()
        pla = str(pla)
    if pla == "yes":
        print("Ok then...")
        play = True
    if pla == "no":
        print ("Ok, your final score was",score,"and you had",cards,"cards left.")
        play = False
while play == True:
    playagain()
"""
                    
"""                    
if play == False:
    score = 0
    cards = 5
    xd = False
    ask = "Would you like to play again?"
    play = True
"""
