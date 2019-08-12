import random

num_digits = 3
max_guesses = 10

def secret_number():
    numbers = list(range(10))
    random.shuffle(numbers)

    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' ,'.join(clues)

def is_only_digits(num):
    
    if num == '':
        return False
    
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9 0'.split():
            return False
    
    return True

print("I am thinking of a %s-digit number. Try to guess what it is." %(num_digits))
print("\nWhen I say:  That means:")
print("Bagels       None of the digits is correct")
print("Pico         One digit is correct but in the wrong position")
print("Fermi        One digit is correct and in the rigt position")

while True:
    secret_num = secret_number()
    print("I have thought up a number. You have %s guesses to get it" %(max_guesses))

    guesses_taken = 1
    while guesses_taken <= max_guesses:
        guess = ''
        while len(guess) != num_digits or not is_only_digits(guess):
            guess = input("\nGuess %s numbers:\n>" %(num_digits))
    
        print(get_clues(guess, secret_num))
        guesses_taken += 1

        if guess == secret_num:
            print("And on your %s try" %(guesses_taken - 1))
            break
        if guesses_taken > max_guesses:
            print("You ran out of guesses. The answers was " + secret_num)

    print("Do you want to play again? (yes or no) ")
    if not input().lower().startswith('y'):
        break
