# Guess the Number Game

A simple Python game where the computer selects a random number between 1 and 20, and the player tries to guess it within 6 attempts.

## How to Play

1. Clone the repository or download the `guss_the_number.py` file.
2. Open a terminal and navigate to the directory containing the file.
3. Run the program using the command: `python guss_the_number.py`
4. Follow the prompts to play the game. Enter your name and try to guess the secret number within 6 attempts.

## Gameplay Rules

- The computer randomly selects a secret number between 1 and 20.
- You have a maximum of 6 attempts to guess the correct number.
- After each guess, the program provides feedback on whether your guess is too high or too low.
- If you correctly guess the number within the allowed attempts, you win!
- If you run out of attempts, the program reveals the secret number and you lose.

## Example

```shell
Hello! What is your name?
Alice
Well, Alice, I am thinking of a number between 1 and 20.
Take a guess: 10
Your guess is too high.
Take a guess: 5
Your guess is too low.
Take a guess: 8
Congratulations! You found my number in 3 guesses.
