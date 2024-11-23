import random
print("There are 3 boxes buried along a 7km path")
print("Your task is to guess the correct locations of the boxes.")
print("If you guess wrong, the boxes will move to new locations.")
box_locations = [random.randint(1,7), random.randint(1,7), random.randint(1,7)]
box_weights = [200, 300, 213]
total_weight = sum(box_weights)   
while True:
    print('Enter your guesses for where the boxes are buried (0-7km)')
    guesses = input("Enter three numbers separated by spaces (e.g., 1 3 5): ").split()
    guesses = list(map(int, guesses)) 
    if sorted(guesses) == sorted(box_locations):
        print('Congratulations, You found all the boxes!')
        break
    else:
        print('Wrong guesses! The boxes are moving to new spots...')
        box_locations = [random.randint(0,7), random.randint(1,7), random.randint(1,7)]