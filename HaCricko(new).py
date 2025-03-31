import random  # Importing the random module for generating random numbers
import sys  # Importing sys module for exiting the program
from Functions import P_toss, C_toss  # Importing toss functions from Functions.py
from Functions import inputvalidation  # Importing input validation function from Functions.py

while True:

    print("Hacricko Version 2.0.0")
    print("---Menu---")
    print("1. To start new game")
    print("2. See previous Scores")  # Feature will be added soon
    print("3. Exit")

    menu_choice = inputvalidation([1, 2, 3])  # Get the user's menu choice using input validation

    if menu_choice == 1:
        # Ask for who starts the game
        print("coach 🧢: Type '1' if you want to start or '2' if you want computer to start")
        game_choice = inputvalidation([1, 2])  # Get the user's choice for who starts the toss

        if game_choice == 1:
            player_decision, computer_decision = P_toss()
        else:
            computer_decision, player_decision = C_toss()
        

        print("coach 🧢: For how many wickets do you want to play?")
        print("coach 🧢: Choose between 1 to 5 wickets")
        wickets = inputvalidation([1, 2, 3, 4, 5])  # Get the number of wickets from the user
        player_score = []  # List to store player's scores
        computer_score = []  # List to store computer's scores
        player_wickets = 0  # Player's total wickets
        comp_wickets = 0  # Computer's total wickets
        player_runs = 0  # Player's total runs
        comp_runs = 0  # Computer's total runs

        print("Starting Game")

        # Player bats first
        if player_decision == 'Batting':
            # Player's batting phase
            while player_wickets < wickets:
                Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                Computer = random.randint(1, 6)  # Generate computer's number randomly
                print(f"Computer 🤖: {Computer}")

                if Player == Computer:
                    print("Out!")
                    player_wickets += 1
                else:
                    player_runs += Player
                    player_score.append(Player)
                    print(f"runs: {player_runs}")

                #If both players have the same score, it will be a tie and a super over will be played
                if player_runs == comp_runs:
                    print("It's a tie!")
                    print("coach 🧢: Super Over!")

                    super_wickets = 1  # Super Over Wickets
                    super_player_score = []  # List to store player's scores in Super Over
                    super_computer_score = []  # List to store computer's scores in Super Over
                    super_player_wickets = 0  # Player's total wickets in Super Over
                    super_comp_wickets = 0  # Computer's total wickets in Super Over
                    super_player_runs = 0  # Player's total runs in Super Over
                    super_comp_runs = 0  # Computer's total runs in Super Over

                    game_choice = inputvalidation([1, 2])  # Get the user's choice for who starts the toss

                    if game_choice == 1:
                        player_decision, computer_decision = P_toss()
                    else:
                        computer_decision, player_decision = C_toss()

                    if player_decision == 'Batting':
                        # Player's batting phase in Super Over
                        while super_player_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_player_wickets += 1
                            else:
                                super_player_runs += Player
                                super_player_score.append(Player)
                                print(f"runs: {super_player_runs}")

                            if super_player_wickets == super_wickets:
                                print("Player is all out! Computer's turn.")
                                print(f"Target for Computer: {super_player_runs + 1}")
                                break

                        # Computer's batting phase in Super Over
                        while super_comp_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_comp_wickets += 1
                            else:
                                super_comp_runs += Computer
                                super_computer_score.append(Computer)
                                print(f"runs: {super_comp_runs}")

                            # End the game early if the target score is reached
                            if super_comp_runs > super_player_runs:
                                print("Computer won the Super Over!")
                                print("coach 🧢: Better luck next time champ!")
                                break

                            if super_comp_wickets == super_wickets:
                                print("Computer is all out! Player Won the Super Over.")
                                print("coach 🧢: Good game champ!")
                                break

                    else:
                        # Computer's batting phase in Super Over
                        while super_comp_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_comp_wickets += 1
                            else:
                                super_comp_runs += Computer
                                super_computer_score.append(Computer)

                            if super_comp_wickets == super_wickets:
                                print("Computer is all out! Player's turn.")
                                print(f"Target for Player: {super_comp_runs + 1}")
                                break

                        # Player's batting phase in Super Over
                        while super_player_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_player_wickets += 1
                            else:
                                super_player_runs += Player
                                super_player_score.append(Player)

                            # End the game early if the target score is reached
                            if super_player_runs > super_comp_runs:
                                print("Player won the Super Over! 🏆")
                                print("coach 🧢: Good game champ!")
                                break

                            if super_player_wickets == super_wickets:
                                print("Player is all out! Computer Won the Super Over.")
                                print("coach 🧢: Better luck next time champ!")
                                break
                if player_wickets == wickets:
                    print("Player is all out! Computer's turn.")
                    print("coach 🧢: Better luck next time champ!")
                    break

            # Computer's batting phase
            while comp_wickets < wickets:
                Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                Computer = random.randint(1, 6)  # Generate computer's number randomly
                print(f"Computer 🤖: {Computer}")

                if Player == Computer:
                    print("Out!")
                    comp_wickets += 1
                else:
                    comp_runs += Computer
                    computer_score.append(Computer)
                    print(f"runs: {comp_runs}")

                # End the game early if the target score is reached
                if comp_runs > player_runs:
                    print("Computer won!")
                    print("coach 🧢: Better luck next time champ!")
                    break

                if comp_wickets == wickets:
                    print("Computer is all out! Player Won.")
                    print("coach 🧢: Good game champ!")
                    break

        # Computer bats first
        else:
            # Computer's batting phase
            while comp_wickets < wickets:
                Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                Computer = random.randint(1, 6)  # Generate computer's number randomly
                print(f"Computer 🤖: {Computer}")

                if Player == Computer:
                    print("Out!")
                    comp_wickets += 1
                else:
                    comp_runs += Computer
                    computer_score.append(Computer)

                if comp_wickets == wickets:
                    print("Computer is all out! Player's turn.")
                    print(f"Target for Player: {comp_runs + 1}")
                    break

            # Player's batting phase
            while player_wickets < wickets:
                Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                Computer = random.randint(1, 6)  # Generate computer's number randomly
                print(f"Computer 🤖: {Computer}")

                if Player == Computer:
                    print("Out!")
                    player_wickets += 1
                else:
                    player_runs += Player
                    player_score.append(Player)

                # End the game early if the target score is reached
                if player_runs > comp_runs:
                    print("Player won! 🏆")
                    print("coach 🧢: Good game champ!")
                    break
                #If both players have the same score, it will be a tie and a super over will be played 
                if player_runs == comp_runs:

                    print("It's a tie!")
                    print("coach 🧢: Super Over!")    
                    
                    super_wickets = 1  # Super Over Wickets
                    super_player_score = []  # List to store player's scores in Super Over
                    super_computer_score = []  # List to store computer's scores in Super Over
                    super_player_wickets = 0  # Player's total wickets in Super Over
                    super_comp_wickets = 0  # Computer's total wickets in Super Over
                    super_player_runs = 0  # Player's total runs in Super Over
                    super_comp_runs = 0  # Computer's total runs in Super Over

                    game_choice = inputvalidation([1, 2])  # Get the user's choice for who starts the toss

                    if game_choice == 1:
                        player_decision, computer_decision = P_toss()
                    else:
                        computer_decision, player_decision = C_toss()

                    if player_decision == 'Batting':
                        # Player's batting phase in Super Over
                        while super_player_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_player_wickets += 1
                            else:
                                super_player_runs += Player
                                super_player_score.append(Player)
                                print(f"runs: {super_player_runs}")

                            if super_player_wickets == super_wickets:
                                print("Player is all out! Computer's turn.")
                                print(f"Target for Computer: {super_player_runs + 1}")
                                break

                        # Computer's batting phase in Super Over
                        while super_comp_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_comp_wickets += 1
                            else:
                                super_comp_runs += Computer
                                super_computer_score.append(Computer)
                                print(f"runs: {super_comp_runs}")

                            # End the game early if the target score is reached
                            if super_comp_runs > super_player_runs:
                                print("Computer won the Super Over!")
                                print("coach 🧢: Better luck next time champ!")
                                break

                            if super_comp_wickets == super_wickets:
                                print("Computer is all out! Player Won the Super Over.")
                                print("coach 🧢: Good game champ!")
                                break

                    else:
                        # Computer's batting phase in Super Over
                        while super_comp_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_comp_wickets += 1
                            else:
                                super_comp_runs += Computer
                                super_computer_score.append(Computer)

                            if super_comp_wickets == super_wickets:
                                print("Computer is all out! Player's turn.")
                                print(f"Target for Player: {super_comp_runs + 1}")
                                break

                        # Player's batting phase in Super Over
                        while super_player_wickets < super_wickets:
                            Player = inputvalidation([1, 2, 3, 4, 5, 6])  # Get player's number (1-6)
                            Computer = random.randint(1, 6)  # Generate computer's number randomly
                            print(f"Player 🧑: {Player}, Computer 🤖: {Computer}")

                            if Player == Computer:
                                print("Out!")
                                super_player_wickets += 1
                            else:
                                super_player_runs += Player
                                super_player_score.append(Player)

                            # End the game early if the target score is reached
                            if super_player_runs > super_comp_runs:
                                print("Player won the Super Over! 🏆")
                                print("coach 🧢: Good game champ!")
                                break

                            if super_player_wickets == super_wickets:
                                print("Player is all out! Computer Won the Super Over.")
                                print("coach 🧢: Better luck next time champ!")
                                break

                if player_wickets == wickets:
                    print("Player is all out! Computer Won.")
                    print("coach 🧢: Better luck next time champ!")
                    break

        # Display final stats
        print("--Final Stats--")
        print(f"Player: {player_runs}/{player_wickets}")
        print(f"Computer: {comp_runs}/{comp_wickets}")

    elif menu_choice == 2:
        print("Feature to view previous scores is not implemented yet.")

    elif menu_choice == 3:
        print("Exiting the program. Goodbye!")
        sys.exit()
