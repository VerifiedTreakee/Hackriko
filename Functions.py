import random  # Importing the random module for generating random numbers

# Function to validate player input
def inputvalidation(valid_list):
    while True:
        try:
            # Get input from the user
            Player = int(input(f"Enter your number {valid_list}: "))
            if Player not in valid_list:
                raise ValueError  # Raise error if input is invalid
            return Player  # Return valid input
        except ValueError:
            print("coach 🧢: Invalid Input. Try again champ!")  # Prompt for valid input if error occurs


# Function for Player's toss
def P_toss():
    print("Initializing toss 🪙")
    print("coach 🧢: Type '1' for Even or '2' for Odd")
    print("odd ya eve?")
    # Use inputvalidation to get valid input for player's choice (Even or Odd)
    pl = inputvalidation([1, 2])  # Player chooses Even (1) or Odd (2)
    print(f"Player chooses {'Even' if pl == 1 else 'Odd'}")

    # Use inputvalidation to get valid input for player's toss number (1-6)
    pl_toss = inputvalidation([1, 2, 3, 4, 5, 6])  # Player enters a number between 1 and 6
    print("Player:", pl_toss)

    com_toss = random.randint(1, 6)  # Generate computer's toss number randomly
    print("Computer:", com_toss)

    # Determine the result of the toss (Even or Odd)
    t = 1 if (pl_toss + com_toss) % 2 == 0 else 2

    # Check if the player won the toss
    if t == pl:
        print("Player won the toss 🏆")

        # Use inputvalidation to get valid input for player's decision (Batting or Bowling)
        print("coach 🧢: Type '1' to Bat 🏏 or '2' to Bowl 🥎")
        decision = inputvalidation([1, 2])

        if decision == 1:
            print("Player chooses to Bat 🏏")
            return 'Batting', 'Bowling'
        else:
            print("Player chooses to Bowl 🥎")
            return 'Bowling', 'Batting'
    else:
        print("Computer won the toss 🪙")
        com_decision = random.choice(['Batting 🏏', 'Bowling 🥎'])  # Added emojis to match C_toss
        print(f"Computer chooses to {com_decision}")
        return com_decision, 'Batting' if com_decision == 'Bowling 🥎' else 'Bowling'


# Function for Computer's toss
def C_toss():
    print("Computer starts the game 🪙")
    x = random.randint(1, 2)  # Computer randomly chooses Even (1) or Odd (2)
    pl = 2 if x == 1 else 1  # Player gets the opposite choice
    print(f"Computer chooses {'Even' if x == 1 else 'Odd'}")

    # Use inputvalidation to get valid input for player's toss number (1-6)
    pl_toss = inputvalidation([1, 2, 3, 4, 5, 6])  # Player enters a number between 1 and 6
    print("Player:", pl_toss)

    com_toss = random.randint(1, 6)  # Generate computer's toss number randomly
    print("Computer:", com_toss)

    # Determine the result of the toss (Even or Odd)
    t = 1 if (pl_toss + com_toss) % 2 == 0 else 2

    # Check if the player won the toss
    if t == pl:
        print("Player won the toss 🏆")

        # Use inputvalidation to get valid input for player's decision (Batting or Bowling)
        print("coach 🧢: Type '1' to Bat 🏏 or '2' to Bowl 🥎")
        decision = inputvalidation([1, 2])
        if decision == 1:
            print("Player chooses to Bat 🏏")
            return 'Batting', 'Bowling'
        else:
            print("Player chooses to Bowl 🥎")
            return 'Bowling', 'Batting'
    else:
        print("Computer won the toss 🪙")
        com_decision = random.choice(['Batting 🏏', 'Bowling 🥎'])  # Computer randomly chooses Batting or Bowling
        print(f"Computer chooses to {com_decision}")
        return com_decision, 'Batting' if com_decision == 'Bowling 🥎' else 'Bowling'


# Function to display the scoreboard
def display_scoreboard(runs, wickets):
    print(f"Score: {runs}/{wickets}")

