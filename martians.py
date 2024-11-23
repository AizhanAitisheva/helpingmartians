import random

print("There are 3 boxes buried along a 7km path.")
print("Your task is to guess the correct locations of the boxes.")
print("If you guess wrong, the boxes will move to new locations.")

box_locations = [random.sample(1, 8),3 for _ in range(3)]
box_weights = [200, 300, 213]
total_weight = sum(box_weights)

while True:
    try:
        print("\nEnter the kilometers where you think the cargo is buried (1-7):")

        guess1 = int(input("First location: "))
        if not (1 <= guess1 <= 7):
            print("The location must be between 1 and 7. Please try again.\n")
            continue

        guess2 = int(input("Second location: "))
        if not (1 <= guess2 <= 7):
            print("The location must be between 1 and 7. Please try again.\n")
            continue

        guess3 = int(input("Third location: "))
        if not (1 <= guess3 <= 7):
            print("The location must be between 1 and 7. Please try again.\n")
            continue

    except ValueError:
        print("Please enter valid numbers between 1 and 7.\n")
        continue

    guesses = [guess1, guess2, guess3]

    if sorted(guesses) == sorted(box_locations):
        print(f"\nCongratulations, You found all the boxes!")
        print(f"The boxes were at: {box_locations}")
        break
    else:
        
        correct_guesses = len(set(guesses) & set(box_locations))
        print(f"\nYou guessed {correct_guesses} location(s) correctly.")
        print("Wrong guesses! The boxes are moving to new spots...")
        box_locations = [random.sample(1, 8),3 for _ in range(3)]
