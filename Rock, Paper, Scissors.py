import random
choice = ["ROCK", "PAPER", "SCISSORS"]
plist = []
clist = []

ro = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
pa = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
sci = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    pscore = 0
    cscore = 0
    for i in plist:
        pscore = pscore + 1
    for t in clist:
        cscore = cscore + 1
    print('''
Here are the scores! 
You: ''' + str(pscore) + " Computer: " + str(cscore))
    x = input('''
Rock/Paper/Scissors?
''')
    y = random.choice(choice)
    if x == "rock":
        print("You have chosen... Rock!")
        print(ro)
        print("The computer has chosen... " + y)
        if y == "ROCK":
            print(ro)
            print("It's a TIE!")
        elif y == "PAPER":
            print(pa)
            clist.append("")
            print("You loose")
        else:
            print(sci)
            plist.append("E")
            print("You win!")
    elif x == "paper":
        print("You have chosen... Paper!")
        print(pa)
        print("The computer has chosen... " + y)
        if y == "PAPER":
            print(pa)
            print("It's a TIE!")
        elif y == "SCISSORS":
            print(sci)
            clist.append("E")
            print("You loose")
        else:
            print(ro)
            plist.append("E")
            print("You win!")
    elif x == "scissors":
        print("You have chosen... Scissors!")
        print(sci)
        print("The computer has chosen... " + y)
        if y == "SCISSORS":
            print(sci)
            print("It's a TIE!")
        elif y == "ROCK":
            print(ro)
            clist.append("E")
            print("You loose")
        else:
            print(pa)
            plist.append("E")
            print("You win!")
    elif x == "torren":
        print("You fool... you have chosen " + x)
        print("You have lost...")
        clist.append("E")
    else:
        print("Invalid input, try again")
