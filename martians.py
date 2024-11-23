import random


print("There are 3 boxes buried along a 7km path.")
print("Your task is to guess the correct locations of the boxes.")
print("If you guess wrong, the boxes will move to new locations.")

box_locations = random.sample(range(1, 8), 3)
box_weights = [200, 300, 213]
total_weight = sum(box_weights)

def get_valid_guess(promt):
    while True:
        try:
            guess = int(input(promt))
            if 1 <= guess <= 7:
                return guess
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

while True:

    guess1 = get_valid_guess("First location: ")
    guess2 = get_valid_guess("Second location: ")
    guess3 = get_valid_guess("Third location: ")
    
    guesses = [guess1, guess2, guess3]

    if set(guesses) == set(box_locations):
        print(f"\nCongratulations, You found all the boxes!")
        print(f"The boxes were at: {box_locations}")
        break
    else:
        correct_locations = set(guesses) & set(box_locations)
        correct_guesses = len(correct_locations)
        print(f"\nYou guessed {correct_guesses} location(s) correctly.")
        print("Wrong guesses! The boxes are moving to new spots...")
        box_locations = random.sample(range(1,8), 3)
