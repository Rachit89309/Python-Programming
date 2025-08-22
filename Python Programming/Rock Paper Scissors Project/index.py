# Rules -
# rock wins against scissors
# scissors win against paper
# paper wins against rock

# 0 for rock
# 1 for paper
# 2 for scissors

import random
rock = '''
******
*     *
*     *
******
*  *  
*   * 
*    *

'''
paper='''
******
*     *
*     *
******
*
*
*

'''
scissors='''
 *****
*     
*     
 *****
      *
      *
 *****

'''

game_images = [rock, paper, scissors]
flag=True
while(flag):
    user_choice = int(input("Enter your choice : Type 0 for Rock, 1 for Paper, 2 for Scissors  "))
    if user_choice >=3 or user_choice < 0:
        print("You entered invalid number, You lose.")
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print("Computer Choose :")
        print(game_images[computer_choice])
        if computer_choice == user_choice:
            print("It's a draw")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif user_choice == 0 and computer_choice == 2:
            print("You win")      
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win")
    choice=str(input('If you want to exit press E or e else press any key to continue: '))
    if(choice=='E'or choice=='e'):
        flag=False
              








# user_choice = int(input("Enter your choice : Type 0 for Rock, 1 for Paper, 2 for Scissors  "))
# if user_choice >=3 or user_choice < 0:
#     print("You entered invalid number, You lose.")
# else:
#     print(game_images[user_choice])
#     computer_choice = random.randint(0, 2)
#     print("Computer Choose :")
#     print(game_images[computer_choice])
#     if computer_choice == user_choice:
#         print("It's a draw")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif user_choice == 0 and computer_choice == 2:
#         print("You win")      
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win")
              