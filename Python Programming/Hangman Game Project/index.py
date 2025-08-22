#                              +---------------+
#                               |     Start     |
#                               +---------------+
#                                       |
#                                       v
#                        +-----------------------------+
#                        |    Generate a word          |
#                        +-----------------------------+
#                                       |
#                                       v
#              +------------------------------------------+
#              | Generate as many blanks as letters       |
#              |                  in word                 |
#              +------------------------------------------+
#                                       |
#                                       v
#                              +----------------+
#     ------------------------|  Guess a letter|-------------------------
#     |                         +----------------+                       |
#     |                                  |                               | 
#     |                                  v                               |
#     |                   +-------------------------------+              |
#     |                   |   Is guessed letter in word?  |              |
#     |                   +-------------------------------+              |
#     |                        /               \                         | 
#     |                       /                 \                        |
#     |                     Yes                 No                       |
#     |                      |                   |                       |
#     |                      v                   v                       |
#     |        +-------------------------+    +------------+             |
#     |        | Replace blank with      |    | Lose a life|             |
#     |        | guessed letters         |    +------------+             |
#     |        +-------------------------+          |                    |
#     |                      |                      v                    |
#     |                      v             +------------------+     No     | 
#     | No    +---------------------------------+  | Out of lives?|-------
#     ---- |  Are all blanks filled?         |  +------------------+
#          +---------------------------------+           |
#           |                |                             Yes
#           |                v                               |
#           |  Yes   +---------------------+                   |
#           |-----|       End           |<------------------+
#                 +---------------------+



import random

word_list = ["apple", "beautiful", "potato"]
chosen_word = random.choice(word_list)
print(chosen_word)

stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    '''
]

display = []
for i in range(len(chosen_word)):
    display += '_'
print(display) 


game_over = False
lives = len(stages) - 1
while not game_over:
    guessed_letter = input("Guess a letter : ").lower()
    if guessed_letter in chosen_word:
     for position in range(len(chosen_word)):
      
       if chosen_word[position] == guessed_letter:
         display[position] = guessed_letter
    else:
       lives -= 1
       print(f"Incorrect guess. You have {lives} lives left.") 
    print(display)      
    print(stages[len(stages) - 1 - lives])

    if '_' not in display:
       game_over =True
       print("You win")

    if lives == 0:
       game_over = True
       print("You lose")
       print(f"The word was : {chosen_word}")   