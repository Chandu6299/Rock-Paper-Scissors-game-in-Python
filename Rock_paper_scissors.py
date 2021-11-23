
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

#Write your code below this line 👇
my = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if my == 0:
  print(rock)
elif my == 1:
  print(paper)
else:
  print(scissors)

computer = random.randint(0,2)

# print("\nComputer chose: ")

if my < 0 or my >= 3 :
  print("Invalid Entry, You lose")

else:
  print("\nComputer chose: ")
  if computer == 0:
    print(rock)
  elif computer == 1:
    print(paper)
  else:
    print(scissors)

  if my == 0 :
    if computer == 2:
      print("You won")
    elif computer == 0:
      print("Its a Draw")
    else:
      print(" You lose")

  if my == 1 :
    if computer == 0:
      print("You won")
    elif computer == 1:
      print("Its a Draw")
    else:
        print(" You lose")

  if my == 2 :
    if computer == 1:
     print("You won")
    elif computer == 2:
      print("Its a Draw")
    else:
      print(" You lose")