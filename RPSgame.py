#  Welcome to my Rock, Paper, Scissor Game

while True:
    print('#' * 30)
    print('-----ROCK PAPER SCISSOR v.1---')
    print('#' * 30)

    items = ["scissor", "paper", "rock"]

    print("Enter player 1's choice: ")
    p1_choice = input()

    for i in range(10):
        print("NO CHEATING!")

    print("Enter player 2's choice: ")
    p2_choice = input()

    if p1_choice == items[0] and p2_choice == items[1]:
        print('Player 1 WINS!')
    elif p1_choice == items[0] and p2_choice == items[2]:
        print('Player 2 WINS!')
    elif p1_choice == items[0] and p2_choice == items[0]:
        print('DRAW!')

    # If player 1 choose PAPER
    elif p1_choice == items[1] and p2_choice == items[0]:
        print('Player 2 WINS!')
    elif p1_choice == items[1] and p2_choice == items[1]:
        print('DRAW!')
    elif p1_choice == items[1] and p2_choice == items[2]:
        print('Player 1 WINS!')
    elif p1_choice == items[2] and p2_choice == items[0]:
        print('Player 1 WINS')
    elif p1_choice == items[2] and p2_choice == items[1]:
        print('Player 2 WINS!')
    elif p1_choice == items[2] and p2_choice == items[2]:
        print('DRAW!')

