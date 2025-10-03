# 🎮 Tic-Tac-Toe with AI (Python)

A classic **Tic-Tac-Toe game** built entirely in Python using the `tkinter` library, where a human player competes against an **AI opponent** powered by the **Minimax algorithm**. The game includes a clean graphical interface, automatic win/draw detection, and a restart option — all without using any external libraries or frameworks.

---

## 🧠 Project Description

This project is a beginner-friendly demonstration of how to build a complete **Tic-Tac-Toe game with a graphical user interface (GUI)** and **AI opponent** using only Python’s standard libraries.

It combines three key components:
- **Game logic**: Validates moves, checks for a winner, and handles draws.
- **Graphical interface**: Uses `tkinter` to provide a user-friendly 3x3 grid for playing.
- **Artificial Intelligence**: Implements the **Minimax algorithm** to ensure the AI always makes the best possible move.

The result is a fun, interactive, and educational project that’s great for learning about Python programming, GUIs, and basic AI techniques.

---

## 📁 Project Overview

- 👤 **Player:** You play as `X`  
- 🤖 **AI:** The computer plays as `O`  
- 🧠 **AI Strategy:** Uses the Minimax algorithm to make optimal decisions  
- 🎯 **Goal:** Get three in a row (horizontally, vertically, or diagonally)

If neither player wins, the game ends in a draw.

---

## ⚙️ Features

- ✅ **Interactive GUI** – Built with `tkinter` for a clean and simple interface.  
- ✅ **AI Opponent** – Uses the **Minimax algorithm** to play perfectly.  
- ✅ **Win/Draw Detection** – Automatically detects and displays results.  
- ✅ **Restart Button** – Instantly resets the board for a new match.  
- ✅ **Lightweight & Dependency-Free** – Works out of the box with Python standard libraries.  

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```Copy code
git clone https://github.com/yourusername/codsoft_taskno.2.git
```
```Copy code
cd tic-tac-toe-ai
```
2. Run the game
Make sure you have Python 3.x installed on your system. Then run:

```Copy code
python tic-tac-toe.py
```
---

💻 Usage Guide
Once the game window opens:

You play as X.

Click any empty square to place your mark.

The AI (playing as O) will instantly respond with its move.

The game ends when:

A player wins 🎉

The board is full (draw 🤝)

Click Restart to play a new round.

🧠 How the AI Works (Minimax Algorithm)
The Minimax algorithm is a classic AI decision-making technique used in turn-based games like Tic-Tac-Toe, Chess, and Checkers. It works by simulating all possible future moves and choosing the one that maximizes the AI’s chance of winning while minimizing the player's chances.

---

🔍 Basic Steps:
Simulate all possible moves for both players.

Assign scores to terminal states:

+1 → AI wins

0 → Draw

-1 → Player wins

Choose the move that maximizes the AI’s minimum possible score (hence “minimax”).

This makes the AI unbeatable — you can only draw or lose.

🧠 Simple Example (Decision Tree):
```
Player (X)
│
├── Move 1
│   ├── AI Wins (+1)
│   └── Draw (0)
│
├── Move 2
│   ├── Player Wins (-1)
│   └── Draw (0)
│
└── Move 3
    ├── Draw (0)
    └── AI Wins (+1)
```
✅ The AI will always choose the path with the highest guaranteed score.
---
📚 Technologies Used
🐍 Python 3.x – Core programming language

🪟 tkinter – GUI framework

🧠 Minimax Algorithm – AI logic
---
🧪 Example Gameplay Session
Here’s what a typical game session might look like:

```Copy code
$ python tic-tac-toe.py
```
[Game Window Opens]

- Player clicks a cell -> 'X' appears
- AI calculates and plays -> 'O' appears
- Game continues until:
   - Player wins 🎉
   - AI wins 🤖
   - It's a draw 🤝

[Popup: "Game Over - It's a draw!"]
Click "Restart" to play again.
🚀 Future Improvements
🧩 Add difficulty levels (Easy, Medium, Hard)

👥 Add a 2-player local mode

📊 Implement score tracking

🎨 Improve the UI with animations, sound effects, and themes
