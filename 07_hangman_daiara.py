import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\\  |
        |
       ===''', '''       
    +---+
    0   |
   /|\\  |
   /    |
       ===''', '''       
    +---+
    0   |
   /|\\  |
   / \\ |
       ===''', '''
    +---+
   [0   |
   /|\\  |
   / \\  |
       ===''', '''
    +---+
   [0]  |
   /|\\  |
   / \\  |
       ===''']              

words = {'Food': ["chocolate cake", "yakissoba", "ice-cream", "pasta carbonara", "soda bread", "pizza"],
'Games': ["super mario world", "ms pac man", "spider-man", "kirby", "tetris", "world of illusion"],
'TV Series': ["stranger things", "the good place", "killing eve", "the great british bake off", "better call saul", "happy"],
'Movies': ["star wars", "indiana jones", "back to the future", "batman", "harry potter", "inside out"],
'Cities': ["dublin", "sao paulo", "london", "newcastle", "napoli", "porto alegre"]}

guessed = []
dict_length = []
for i in words:
    dict_length.append(len(words[i]))

def get_random_word(word_dict):
    while True:
        word_key = random.choice(list(word_dict.keys()))    
        word_index = random.randint(0, len(word_dict[word_key]) - 1)
        if word_dict[word_key][word_index] not in guessed:
            return [word_dict[word_key][word_index], word_key]

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('Missed letters:', end='')
    for letter in missed_letters:
        print(letter, end='')
    print()
    blanks = '_' * len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end='')
    print()

def get_guess(already_guessed):
    while True:
        print("Guess a letter:")
        guess = input(">").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You already guessed that letter. Try again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    print("Would you like to play again?")
    return input(">").lower().startswith('y')

print(" H A N G M A N\n(but with levels)")

difficulty = 'X'
while difficulty not in 'EMH':
    difficulty = input("Enter difficulty: E - Easy, M - Medium, H - Hard\n>").upper()

if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
    
missed_letters = ''
correct_letters = "-' "
secret_word, secret_set = get_random_word(words)
guessed.append(secret_word)
game_is_done = False


win = 0
loses = 0 #changes
while True:
    if difficulty == 'E':
        print("Your tip is: " + secret_set)
    if difficulty == 'M':
        print("Your word is in one of these categories: " + ', '.join(words.keys()))
    display_board(missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            win += 1
            print("Yes! The secret word is " + secret_word + "! You won!")
            game_is_done = True
    else:
        missed_letters = missed_letters + guess
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            loses += 1
            display_board(missed_letters, correct_letters, secret_word)
            print("You have run out of guesses!\nAfter " + str(len(missed_letters)) + " missed guesses and " + str(len(correct_letters) - 3) + " of correct guesses, the word was " + secret_word)
            game_is_done = True
    if game_is_done:
        if len(guessed) != sum(dict_length):
            if play_again():
                missed_letters = ''
                correct_letters = "-' "
                secret_word, secret_set = get_random_word(words)
                guessed.append(secret_word)
                game_is_done = False
            else:
                print("Wins: " + str(win) + " | Loses: " + str(loses))
                break
        else:
            print("Wins: " + str(win) + " | Loses: " + str(loses))
            break