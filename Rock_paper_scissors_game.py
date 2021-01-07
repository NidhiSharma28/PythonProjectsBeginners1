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

choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
if choice==0:
 print(rock)
elif choice==1:
  print(paper)
elif choice ==2:
  print(scissors)
else:
  print("Oops!wrong choice")
computer = random.randint(0,2)
if computer==0:
 print(rock)
elif computer==1:
  print(paper)
else: 
  print(scissors)
  #conditions
if choice==0: 
  if computer==1:
   print("You lost!")
  elif computer==2:
    print("You win!")
  else:
    print("It\'s a draw")
elif choice==1: 
  if computer==0:
   print("You win!")
  elif computer==2:
    print("You lost!")
  else:
    print("It\'s a draw")
elif choice==2: 
  if computer==0:
   print("You lost!")
  elif computer==1:
    print("You win!")
  else:
    print("It\'s a draw")
else:
  print("Game Over.")

