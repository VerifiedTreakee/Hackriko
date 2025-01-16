import random
import sys
from Funtions import P_toss, C_toss

while True:
    print("Hacricko version idk")
    print("---Menu---")
    print("1. To start new game")
    print("2. See previous Scores")
    print("3. Exit")

    try:
        menu = int(input("Enter a choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if menu == 1:
        while True:
            try:
                P = int(input("Press 1 if you want to start or 2 if you want computer to start\n"))
                if P not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input. Please Enter 1 for you to start or 2 for computer to start!")

        if P == 1:
            p_choice, c_choice = P_toss()
        else:
            p_choice, c_choice = C_toss()

        print("Starting Game")
        Player_Score = []
        Comp_Score = []

        if p_choice == 'Batting':
            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    Player_Score.append(Player)
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)

                    if Player == Computer:
                        print("Bold \nComputer's turn")
                        print("Target:", sum(Player_Score) + 1)
                        break
                except ValueError:
                    print("Invalid Input. Please try again.")

            while True:
                Computer = random.randint(1, 6)
                print("Computer:", Computer)
                Comp_Score.append(Computer)

                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    if Computer == Player:
                        print("Bold")
                        print("Player Won")
                        break
                    elif sum(Comp_Score) > sum(Player_Score):
                        print("Computer won")
                        break
                except ValueError:
                    print("Invalid Input. Please try again.")

            print("--Stats--")
            print("Player:", sum(Player_Score))
            print("Computer:", sum(Comp_Score))

        else:
            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)
                    Comp_Score.append(Computer)

                    if Player == Computer:
                        print("Bold \nPlayer's turn")
                        print("Target:", sum(Comp_Score) + 1)
                        break
                except ValueError:
                    print("Invalid Input. Please try again.")

            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    Player_Score.append(Player)
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)

                    if Player == Computer:
                        print("Bold")
                        print("Computer Won")
                        break
                    elif sum(Player_Score) > sum(Comp_Score):
                        print("Player won")
                        break
                except ValueError:
                    print("Invalid Input. Please try again.")

            print("--Stats--")
            print("Player:", sum(Player_Score))
            print("Computer:", sum(Comp_Score))

    elif menu == 2:
        print("Feature not implemented yet.")
    elif menu == 3:
        sys.exit("Exiting the program.")
    else:
        print("Invalid input. Would you like to re-run the game? (y/n)")
        n = input("Enter Choice: ").strip().lower()
        if n[0] == 'y':
            continue
        else:
            sys.exit("Exiting the program.")
