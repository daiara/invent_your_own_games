import random

print("Hi! This is a Guess the Number game.")
name = input("\nWhat's your name? ")

number = random.randint(0,20)
count = 0

print("\nHello, " + name + ". Guess which number I'm thinking: ")

while True:
    count += 1
    guess = int(input(">"))
    if count < 5:
        if guess > number:
            print("Too high. Try again: ")
        if guess < number:
            print("Too low. Try again:")
        if guess == number:
            print("Spot on!")
            print("\nCongratulations, " + name + "! It took you " + str(count) + " times to guess it :)")
            break
    if count == 5:
        print("Sorry, you reached your limit. The number was " + str(number))
        break