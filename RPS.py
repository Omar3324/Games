import random
paper = 1
rock  = 2
scissor = 3

rules = input("""press Enter to continue or type (Help) for the rules: """).lower()

if rules == "help":
    print("""          
                      ******Rules******
            1- YOU CHOOSE AND THE COMPUTER CHOOSES
            2- ROCK SMASHES SCISSORS ->    ROCK WIN
            3- SCISSORS CUT PAPER    ->    SCISSORS WIN
            4- PAPER COVERS ROCK     ->    PAPER WIN""")
    
user = int(input("enter you choice((1- paper), (2-rock), (3-scissor) (choose the number)): "))

if user == rock:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user == paper:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif user == scissor:
    print("""
        _______
---'   ____)____
          ______)
       __________)
      (____) 
---.__(___)
    """)
else:
    print("invalid")

x = random.randint(1,3)
if x == rock:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif x == paper:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif x == scissor:
    print("""
        _______
---'   ____)____
          ______)
       __________)
      (____) 
---.__(___)
    """)
else:
    print("invalid")


if user == paper and x == rock or user == rock and x == scissor or user == scissor and x == paper:
    print("""
you win
""")
elif x == user:
    print("""
you tied
""")
else:
    print("you lose")


    