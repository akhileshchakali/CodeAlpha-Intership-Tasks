# Task 1 - Hangman Game

## 📌 Project Description

This project is a simple **text-based Hangman Game** developed using Python.

The player has to guess the letters of a randomly selected country or place name. The player gets a maximum of **6 incorrect guesses**. For every incorrect guess, a part of the Hangman is displayed.

## 🎯 Objective

The objective of this task is to create a basic console-based game using Python and practice concepts such as:

* Random selection
* Lists
* Strings
* Loops
* Conditional statements
* User input
* Basic game logic

## 🛠️ Technologies Used

* **Python**
* `random` module

## 🎮 How the Game Works

1. The program contains a predefined list of country and place names.
2. A word is randomly selected using Python's `random.choice()`.
3. The selected word is initially displayed using underscores.
4. The player enters a letter as a guess.
5. If the guessed letter exists in the word, its correct position is revealed.
6. If the guessed letter is incorrect, one life is lost and the Hangman drawing changes.
7. The player has a maximum of **6 incorrect guesses**.
8. The player wins when all letters are correctly guessed.
9. The player loses when all 6 chances are used.

## 📂 Project Structure

```text
 Task_1_Hangman/
    │
    ├── hangman.py
    ├── README.md
    └── VIDEO_LINK.md

```

## ▶️ How to Run

Make sure Python is installed on your system.

Open the terminal inside the project folder and run:

```bash
python hangman.py
```

## 💡 Sample Gameplay

```text
        Hangman Game
******************************
Guess Country Name

_ _ _ _

Enter a word : a

_ _ _ a

Enter a word : z

    +---+
    |   |
    0   |
   /|   |
        |
        |
---------

_ _ _ a
```

The game continues until the player either guesses the complete word or uses all 6 chances.

## ✨ Features

* Random word selection
* Console-based gameplay
* Maximum 6 incorrect guesses
* Displays the correct word when the player loses
* Displays a winning message when the word is completely guessed

## 📚 Python Concepts Used

* `import random`
* Lists
* Strings
* `random.choice()`
* `while` loop
* `for` loop
* `if-else` statements
* `input()`
* String indexing
* List modification
* `break`

## 👨‍💻 Internship Task

**Internship:** CodeAlpha Internship
**Task:** Task 1 - Hangman Game
**Language:** Python
