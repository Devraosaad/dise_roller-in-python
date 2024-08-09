import random

def roll_dice():
    return random.randint(1, 6)

def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")

        roll_again = input("Do you want to roll again? (yes/no): ").lower()
        if roll_again != 'yes':
            print("Thank you for using the Dice Rolling Simulator. Goodbye!")
            break

if __name__ == "__main__":
    dice_rolling_simulator()
