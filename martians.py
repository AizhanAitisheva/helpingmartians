import random
print("There are 3 boxes buried along a 7km path")
print("Your task is to guess the correct locations of the boxes.")
print("If you guess wrong, the boxes will move to new locations.")
box_locations = [random.randint(1,7) for _ in range(3)]
box_weights = [200, 300, 213]
total_weight = sum(box_weights)   
while True:
    try:
        print("Enter the kilometers where you think the cargo is buried:")
        guess1 = int(input("First location (0-7): "))
        if not (1 <= guess1 <= 7):
            print("The location must be between 1 and 7. Please try again.\n")
            continue

        guess2 = int(input("Second location (0-7): "))
        if not (1 <= guess2 <= 7):
            print("The location must be between 1 and 7. Please try again.\n")
            continue

        guess3 = int(input("Third location (0-7): "))
        if not (1 <= guess3 <= 7):
            print("The location must be between 1 and 7. Please try again.\n")
            continue

    except ValueError:
        print("Please enter valid numbers between 1 and 7.\n")
        continue

        
    guesses = [guess1, guess2, guess3]

    if sorted(guesses) == sorted(box_locations):
        print('Congratulations, You found all the boxes!')
        break
    else:
        print('Wrong guesses! The boxes are moving to new spots...')
        box_locations = [random.randint(0,7) for _ in range(3)]
