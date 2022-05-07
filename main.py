#Rock-Paper-Scissors
#Developed with 💖 using Python
#Day4 of 100DaysCodingChallenge
#Made with 💖 by Cephas Cardozo

#start_of_code

#imports
import random

#welcome_print
print("ROCK PAPER SCISSORS\n")
print("Developed with 💖 using Python")
print("Created by Cephas Cardozo\n\n")

#rps_game_variables
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

#variables
game_images = [rock, paper, scissors]


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper & 2 for Scissors\n\nType here: "))

#conditionals_/logic
if user_choice >= 3 or user_choice < 0:
  print("You typed an Invalid Number, you LOSE!")
else:
  print(game_images[user_choice])
  print(f"\nYou chose : {user_choice} ")
  
  computer_choice = random.randint(0,2)
  print(game_images[computer_choice])
  print(f"Computer chose : {computer_choice} \n")
  
  
  #conditionals
  if user_choice == 0 and computer_choice == 2:
    print("You WIN!")
  elif computer_choice == 0 and user_choice == 2:
    print("You LOSE!")
  elif computer_choice > user_choice:
    print("You LOSE!")
  elif user_choice > computer_choice:
    print("You WIN!")
  elif computer_choice == user_choice:
    print("Its a DRAW!")


#end_of_code