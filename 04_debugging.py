import random

print('''Since the book teaches about using the debugger on a different
program, I took the example it gave and made a very simple adding game.''')

keep_going = 'yes'
count = 0

while keep_going == 'yes' or keep_going == 'y':
    count += 1
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print("\nWhat is " + str(number1) + " + " + str(number2) + "?")
    answer = int(input(">"))
    if answer == number1 + number2:
        print("Correct!")
    else:
        print("Nope. The answer is " + str(number1 + number2))
    keep_going = input("\nKeep going? (yes or no) ")

if keep_going != 'yes' or keep_going != 'y':
    print("This was fun. You played " + str(count) + " time before getting bored.")