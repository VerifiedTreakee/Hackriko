
## **OPEN SOURCE UNDER**
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
-
# **Hacricko - Relive your School Days**

Hacricko is a Python-based game inspired by the childhood Indian game of "Odd or Even," a cricket variant akin to rock-paper-scissors. Players engage in a toss to decide who bats or bowls first, then compete to score the highest runs without getting bowled out.

---
## **Getting Started**

1. Clone this repository:
   ```bash
   git clone <repository-url>
---

## **How to Play**

### **Main Menu**
1. Launch the game to see the main menu:
   - **Option 1**: Start a new game.
   - **Option 2**: View previous scores (feature not yet implemented).
   - **Option 3**: Exit the game.

---

### **Starting a New Game**
 1. **Choose Who Starts**:
   - Press `1` to start the toss yourself.
   - Press `2` to let the computer start the toss.

---

### **Toss Phase**

#### **If You Start the Toss**
 1. Choose:
   - `1` for **Even**
   - `2` for **Odd**
2. Enter a number between 1 and 6 as your toss input.
3. The computer will randomly select a number.
 4. The sum of the two numbers determines the winner:
   - If the sum is **even** and you chose "Even," you win.
   - If the sum is **odd** and you chose "Odd," you win.

#### **If the Computer Starts the Toss**
1. The computer will randomly choose **Even** or **Odd.**
2. Enter a number between 1 and 6 as your toss input.
3. The winner is determined the same way as above.

#### **Winner's Choice**
- The toss winner chooses to either:
  - **Bat**: Attempt to score as many runs as possible.
  - **Bowl**: Try to restrict the opponent's runs.

---

### **Scoring Phase**

#### **Batting Rules**
1. Input a number between 1 and 6 on each turn.
2. The computer will also choose a random number.
3. If your number matches the computer's number, you are **bowled out**, and your batting ends.
4. Your total score is the sum of all numbers entered before getting out.

#### **Bowling Rules**
1. The computer bats first, and you bowl.
2. Enter a number between 1 and 6 for each ball.
3. If your number matches the computer's number, the computer is **bowled out**, and its batting ends.
4. The computer's total score is the sum of its numbers before getting out.

---

### **Winning the Game**
- The second player attempts to **chase** the target score set by the first player.
- The game ends when:
  - The chasing player scores more than the target (they win).
  - The chasing player is bowled out without exceeding the target (they lose).
- Final scores and game stats are displayed at the end.

---

### **Example Gameplay**

#### **Toss Phase Example**
- Player chooses **Odd** and inputs `3`.
- Computer chooses `4`.
- Total: `3 + 4 = 7` (Odd). The player wins the toss.

#### **Scoring Phase Example**
- Player bats first and inputs:
  - `2`, `4`, `6`. On the fourth input, the player and computer both choose `3` → Bowled out.
  - Player's score: `2 + 4 + 6 = 12`.

- Computer bats and inputs:
  - `1`, `5`, `6`. On the fourth input, the player and computer both choose `4` → Bowled out.
  - Computer's score: `1 + 5 + 6 = 12`.

**Result**: The game is a **tie**.

---

### **Special Notes**
- Input validation ensures all numbers are between 1 and 6.
- Invalid inputs prompt re-entry.
- If the game exits unexpectedly, rerun the program to restart.

---


## Coming soon!

- Highest score
- Game History

