import random
import time

print("Welcome to the Dragon Realm game!")
def display_intro():
    print('''\nYou are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon is
greedy and hungry, andi will eat you on sight.\n''')
    
def choose_cave():
    cave = ''
    while cave != 1 and cave != 2:
        cave = int(input("Which cave will you go into? (1 or 2) "))
    return cave

def check_cave(chosen_cave):
    print("\nYou approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his mouth and...")
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == friendly_cave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    play_again = input("\nDo you want to play again? (yes or no) ")