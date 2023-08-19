import random

# Main function to determine game outcome
def game(comp, you):
    if comp == you:
        return None
    elif comp == 'snake':
        if you == 'water':
            return False
        elif you == 'gun':
            return True
    elif comp == 'water':
        if you == 'gun':
            return False
        elif you == 'snake':
            return True
    elif comp == 'gun':
        if you == 'snake':
            return False
        elif you == 'water':
            return True

# Number of rounds to play
rounds_to_play = 5
comp_wins = 0
user_wins = 0

for i in range(rounds_to_play):
    randNo = random.randint(1, 3)

    if randNo == 1:
        comp = 'snake'
    elif randNo == 2:
        comp = 'water'
    elif randNo == 3:
        comp = 'gun'

    print("Computer has chosen!!")
    print()

    player = input("Your turn:\n1.Snake\n2.Water\n3.Gun\nEnter your choice: ")

    result = game(comp, player)  # Calling Function

    print(f"Computer chose {comp}")
    print(f"You chose {player}")

    # Winner determination
    if result == None:
        print("This game is a tie")
    elif result:
        print("You Win!")
        user_wins += 1
    else:
        print("You lose :(")
        comp_wins += 1
        
    print("-------------------------------------------------------------------")

    print()  # Print an empty line to separate rounds

print("Final Results:")
print(f"Computer wins: {comp_wins}")
print(f"User wins: {user_wins}")
print("Thanks for playing!")
