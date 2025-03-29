import random
import sys
from Funtions import P_toss, C_toss

def display_scoreboard(runs, wickets):
    print(f"\n🏏 Score: {runs} / {wickets}  |  ⚡ Keep going!")

while True:
    print("\n🎮 Hacricko version 0.5dev")
    print("---📜 Menu 📜---")
    print("1️⃣ - Start New Game")
    print("2️⃣ - View Previous Scores")
    print("3️⃣ - Exit 🚪")
    print("4️⃣ Practice Mode 🎯")

    try:
        menu = int(input("Enter a choice: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number between 1-4.")
        continue

    if menu == 1:
        while True:
            try:
                P = int(input("Press 1️⃣ if you want to start or 2️⃣ if computer should start: "))
                if P not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("❌ Invalid input! Enter 1️⃣ to start or 2️⃣ for computer to start.")

        if P == 1:
            p_choice, c_choice, n = P_toss()
        else:
            p_choice, c_choice, n = C_toss()

        print("🚀 Game Started!")
        Player_Score, Comp_Score = [], []
        player_runs = player_wickets = comp_runs = comp_wickets = 0

        if p_choice == 'Batting':
            while True:
                try:
                    Player = int(input("🎯 Enter your number (1-6): "))
                    if Player not in range(1, 7):
                        raise ValueError
                    Player_Score.append(Player)
                    Computer = random.randint(1, 6)
                    print(f"🤖 Computer: {Computer}")

                    if Player == Computer:
                        print("🔥 OUT! Now, Computer bats!")
                        print(f"🎯 Target: {sum(Player_Score) + 1}")
                        break
                    else:
                        player_runs += Player
                        display_scoreboard(player_runs, player_wickets)
                except ValueError:
                    print("❌ Invalid input! Try again.")

            while True:
                try:
                    Player = int(input("🎯 Enter your number (1-6): "))
                    if Player not in range(1, 7):
                        raise ValueError
                    Computer = random.randint(1, 6)
                    print(f"🤖 Computer: {Computer}")
                    Comp_Score.append(Computer)

                    if Computer == Player:
                        print("🔥 OUT!")
                        comp_wickets += 1
                        if comp_wickets >= n:
                            print("💥 All out!")
                            break
                    else:
                        comp_runs += Computer
                        display_scoreboard(comp_runs, comp_wickets)

                    if sum(Comp_Score) > sum(Player_Score):
                        print("🤖 Computer Wins! 🏆")
                        break

                except ValueError:
                    print("❌ Invalid input! Try again.")

            print("📊 Final Scores:")
            print(f"👤 Player: {sum(Player_Score)} 🏏")
            print(f"🤖 Computer: {sum(Comp_Score)} 🏏")

        else:
            while True:
                try:
                    Player = int(input("🎯 Enter your number (1-6): "))
                    if Player not in range(1, 7):
                        raise ValueError
                    Computer = random.randint(1, 6)
                    print(f"🤖 Computer: {Computer}")
                    Comp_Score.append(Computer)

                    if Player == Computer:
                        print("🔥 OUT! Now, Player bats!")
                        print(f"🎯 Target: {sum(Comp_Score) + 1}")
                        break
                    else:
                        comp_runs += Computer
                        display_scoreboard(comp_runs, comp_wickets)
                except ValueError:
                    print("❌ Invalid input! Try again.")

            while True:
                try:
                    Player = int(input("🎯 Enter your number (1-6): "))
                    if Player not in range(1, 7):
                        raise ValueError
                    Player_Score.append(Player)
                    Computer = random.randint(1, 6)
                    print(f"🤖 Computer: {Computer}")

                    if Player == Computer:
                        print("🔥 OUT!")
                        player_wickets += 1
                        if player_wickets >= n:
                            print("💥 All out!")
                            break
                    else:
                        player_runs += Player
                        display_scoreboard(player_runs, player_wickets)

                    if sum(Player_Score) > sum(Comp_Score):
                        print("🎉 Player Wins! 🏆")
                        break

                except ValueError:
                    print("❌ Invalid input! Try again.")

            print("📊 Final Scores:")
            print(f"👤 Player: {sum(Player_Score)} 🏏")
            print(f"🤖 Computer: {sum(Comp_Score)} 🏏")

    elif menu == 2:
        print("📜 Feature not implemented yet!")
    elif menu == 3:
        sys.exit("🚪 Exiting the game. See you soon! 👋")
    elif menu == 4:
        print("🎯 Practice Mode Activated!")
        mode = int(input("Press 1️⃣ for Batting Practice, 2️⃣ for Bowling Practice: "))
        if mode == 1:
            print("🏏 Batting Practice! Unlimited chances.")
            player_runs = 0
            while True:
                try:
                    Player = int(input("🎯 Enter your number (1-6): "))
                    if Player not in range(1, 7):
                        raise ValueError
                    player_runs += Player
                    display_scoreboard(player_runs, 0)
                except ValueError:
                    print("❌ Invalid input! Try again.")
        elif mode == 2:
            print("🎯 Bowling Practice! You need to take 5 wickets.")
            wickets = 0
            while wickets < 5:
                try:
                    Player = int(input("🎯 Enter your number (1-6): "))
                    if Player not in range(1, 7):
                        raise ValueError
                    Computer = random.randint(1, 6)
                    print(f"🤖 Computer: {Computer}")
                    if Player == Computer:
                        print("🔥 OUT!")
                        wickets += 1
                    display_scoreboard(0, wickets)
                except ValueError:
                    print("❌ Invalid input! Try again.")
    else:
        print("❌ Invalid choice! Try again.")