import random
import sys
from Funtions import P_toss
from Funtions import C_toss
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

                if P not in [1,2]:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid Input Please Enter 1 for you to start or 2 for computer to start!")

        if P == 1:
            p_choice,c_choice = P_toss()

        else:
            p_choice,c_choice = C_toss()

   
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
            sys.exit("Invalid Input")
