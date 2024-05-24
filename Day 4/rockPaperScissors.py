import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def choose(value):
    if value == 1:
        print(rock)
    elif value == 2:
        print(paper)
    elif value == 3:
        print(scissors)

symbol = int(input("Choose 1 for Rock, 2 for Paper, 3 for Scissors: "))

choose(symbol)

print("Computers choice:")

computerSymbol = random.randint(1, 3)

choose(computerSymbol)

if symbol == 1 and computerSymbol == 1:
    print("Draw!")
elif symbol == 2 and computerSymbol == 2:
    print("Draw!")
elif symbol == 3 and computerSymbol == 3:
    print("Draw!")
elif symbol == 1 and computerSymbol == 3:
    print("You Win!")
elif symbol == 3 and computerSymbol == 2:
    print("You Win!")
elif symbol == 2 and computerSymbol == 1:
    print("You Win!")

else:
    print("You Loose!")