import random
import time


def print_pause(game_story):
    print(game_story + "\n")
    time.sleep(2)


def intro(villain):
    print_pause("\nYou find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.")


def cave(weapon, villain):
    if weapon == "Sword of Ogoroth":
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good"
                    " stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the"
                    " sword with you.")
        print_pause("You walk back out to the field.")
        weapon = "Sword of Ogoroth"
    field(weapon, villain)


def house(weapon, villain):
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens and"
                f" out steps a {villain}.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} attacks you!")
    if weapon != "Sword of Ogoroth":
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")

    fight_run = validity("Would you like to (1) fight or (2) "
                         "run away?\n", ["1", "2"])
    if fight_run == "1":
        fight(weapon, villain)
    else:
        print_pause("\nYou run back into the field.")
        print_pause("Luckily, you don't seem to have been followed.\n")
        field(weapon, villain)


def fight(weapon, villain):
    if weapon == "Sword of Ogoroth":
        print_pause(f"\nAs the {villain} moves to attack, "
                    "you unsheathe your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the "
                    "attack.")
        print_pause(f"But the {villain} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {villain}.")
        print_pause("You are victorious!!!\n")
        restart()
    else:
        print_pause("\nYou do your best...")
        print_pause(f"but your dagger is no match for the {villain}.")
        print_pause("You have been defeated!\n")
        restart()


def field(weapon, villain):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    house_cave = validity("(Please enter 1 or 2.)\n", ["1", "2"])
    if house_cave == "1":
        house(weapon, villain)
    else:
        cave(weapon, villain)

# validity function checks for invalid input
def validity(question, answers):
    while True:
        choice = input(question).lower()
        if choice in answers:
            return choice
        # User will keep trying till valid input is provided


def restart():
    yes_no = validity("Would you like to play again? (y/n)", ["y", "n"])
    if yes_no == "y":
        print_pause("\n\nExcellent! Restarting the game ...\n")
        play_game()
    else:
        print_pause("\nThanks for playing! See you next time.\n")
