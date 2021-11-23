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

# Write your code below this line 👇
my = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
images = [rock, paper, scissors]

if my < 0 or my >= 3:
    print("Invalid Entry, You lose")

else:
    print(images[my])
    computer = random.randint(0, 2)
    print(f"Computer chose: {images[computer]} ")

    if my == 0 and computer == 2:
        print("You win!")
    elif computer == 1 and my == 0:
        print("You Lose")

    elif computer > my:
        print("You Lose")

    elif my > computer:
        print("You win!")

    elif computer == my:
        print("It's a draw")