import random  # Importing the random module for generating random numbers
import sys  # Importing sys module for exiting the program
from Functions import P_toss, C_toss  # Importing toss functions from Funtions.py
from Functions import display_scoreboard  # Importing display_scoreboard function from Funtions.py


# Main game loop
while True:
    # Display the main menu
    print("Hacricko version 1.2.6")
    print("---Menu---")
    print("1. To start new game")
    print("2. See previous Scores")#feature will be added soon
    print("3. Exit")


    # Get the user's menu choice
    try:
        menu = int(input("Enter a choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Start a new game
    if menu == 1:
        # Get the user's choice for who starts the toss
        while True:
            try:
                P = int(input("Press 1 if you want to start or 2 if you want computer to start\n"))
                if P not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input. Please Enter 1 for you to start or 2 for computer to start!")

        # Perform the toss based on the user's choice
        if P == 1:
            p_choice, c_choice = P_toss()
        else:
            p_choice, c_choice = C_toss()

        print("Starting Game")
        Player_Score = []  # List to store player's scores
        Comp_Score = []  # List to store computer's scores
        player_runs = 0  # Player's total runs
        player_wickets = 0  # Player's total wickets
        comp_runs = 0  # Computer's total runs
        comp_wickets = 0  # Computer's total wickets
        n = 5  # Number of wickets
        # Player bats first
        if p_choice == 'Batting':
            # Player's batting phase
            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    Player_Score.append(Player)
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)

                    if Player == Computer:
                        print("Out! \nComputer's turn")
                        print("Target:", sum(Player_Score) + 1)
                        break
                    else:
                        player_runs += Player
                        display_scoreboard(player_runs, player_wickets)
                except ValueError:
                    print("Invalid Input. Please try again.")

            # Computer's batting phase
            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)
                    Comp_Score.append(Computer)

                    if Computer == Player:
                        print("Out!")
                        comp_wickets += 1
                        if comp_wickets >= n:
                            print("All out!")
                            break
                    else:
                        comp_runs += Computer
                        display_scoreboard(comp_runs, comp_wickets)

                    if sum(Comp_Score) > sum(Player_Score)+1:
                        print("Computer won")
                        break

                except ValueError:
                    print("Invalid Input. Please try again.")

            # Display final stats
            print("--Stats--")
            print("Player:", sum(Player_Score))
            print("Computer:", sum(Comp_Score))

        # Computer bats first
        else:
            # Computer's batting phase
            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)
                    Comp_Score.append(Computer)

                    if Player == Computer:
                        print("Out! \nPlayer's turn")
                        print("Target:", sum(Comp_Score) + 1)
                        break
                    else:
                        comp_runs += Computer
                        display_scoreboard(comp_runs, comp_wickets)
                except ValueError:
                    print("Invalid Input. Please try again.")

            # Player's batting phase
            while True:
                try:
                    Player = int(input("Enter your number (1-6): "))
                    if Player not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError
                    Player_Score.append(Player)
                    Computer = random.randint(1, 6)
                    print("Computer:", Computer)

                    if Player == Computer:
                        print("Out!")
                        player_wickets += 1
                        if player_wickets >= n:
                            print("All out!")
                            break
                    else:
                        player_runs += Player
                        display_scoreboard(player_runs, player_wickets)

                    if sum(Player_Score) > sum(Comp_Score)+1:
                        print("Player won")
                        break

                except ValueError:
                    print("Invalid Input. Please try again.")

            # Display final stats
            print("--Stats--")
            print("Player:", sum(Player_Score))
            print("Computer:", sum(Comp_Score))

    # View previous scores (not implemented)
    elif menu == 2:
        print("Feature not implemented yet.")

    # Exit the program
    elif menu == 3:
        sys.exit("Exiting the program.")

    # Invalid menu input
    else:
        print("Invalid input. Would you like to re-run the game? (y/n)")
        n = input("Enter Choice: ").strip().lower()
        if n[0] == 'y':
            continue
        else:
            sys.exit("Exiting the program.")
