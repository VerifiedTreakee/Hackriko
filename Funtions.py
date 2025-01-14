import random

def P_toss():
    print("Initializing toss")
    print("Type '1' for Even Or '2' for Odd")

    while True:
        try:
            pl = int(input("Odd ya Even?\n"))
            if pl not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter '1' for Even or '2' for Odd.")

    if pl == 1:
        print("Player chooses Even")
    else:
        print("Player chooses Odd")


    while True:
        try:
            pl_toss = int(input("Enter choice (1-6): "))
            if pl_toss < 1 or pl_toss > 6:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

    print("Player:", pl_toss)
    com_toss = random.randint(1, 6)
    print("Computer:", com_toss)

    if (pl_toss + com_toss) % 2 == 0:
        t = 1
    else:
        t = 2

    if t == pl:
        print("Player won the toss")
        while True:
            try:
                c = int(input("Type '1' for Batting or '2' for Bowling: "))
                if c not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter '1' for Batting or '2' for Bowling.")

        if c == 1:
            p_choice = 'Batting'
            c_choice = 'Bowling'
        else:
            p_choice = 'Bowling'
            c_choice = 'Batting'

        print(f"Player won the toss and chooses: {p_choice}")       
    else:
        cc = ["Batting", "Bowling"]
        c_choice = random.choice(cc)
        if c_choice == "Batting":
            p_choice = "Bowling"
        else:
            p_choice = "Batting"
        print(f"Computer won the toss and chooses: {c_choice}")


    return p_choice,c_choice

def C_toss():

    print("Computer starts the game")
    x = random.randint(1,2)

    if x == 1:
        
        print("Computer choose Even")
        pl = 2
    else:
        print("Computer choose Odd")
        pl = 1

    
    com_toss = random.randint(1, 6)
    print("Computer:", com_toss)
    
    while True:
        try:
            pl_toss = int(input("Enter choice (1-6): "))
            if pl_toss < 1 or pl_toss > 6:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

    if (pl_toss + com_toss) % 2 == 0:
        t = 1
    else:
        t = 2

    if t == pl:
        print("Player won the toss")
        while True:
            try:
                c = int(input("Type '1' for Batting or '2' for Bowling: "))
                if c not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter '1' for Batting or '2' for Bowling.")

        if c == 1:
            p_choice = 'Batting'
            c_choice = 'Bowling'
        else:
            p_choice = 'Bowling'
            c_choice = 'Batting'

        print(f"Player won the toss and chooses: {p_choice}")       
    else:
        cc = ["Batting", "Bowling"]
        c_choice = random.choice(cc)
        if c_choice == "Batting":
            p_choice = "Bowling"
        else:
            p_choice = "Batting"
        print(f"Computer won the toss and chooses: {c_choice}")
        
    return p_choice,c_choice
