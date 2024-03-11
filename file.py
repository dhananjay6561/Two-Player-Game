import random

def guess_game():
    print("Welcome to the Two-Player Guessing Game!")

    # This will generate a random secret number between 1 to 20
    secret_number = random.randint(1, 20)

    # Initialize player guesses
    player1_guess = 0
    player2_guess = 0

    while player1_guess != secret_number and player2_guess != secret_number:
        # Player 1's turn
        player1_guess = int(input("Player 1, enter your guess (between 1 and 20): "))
        if player1_guess == secret_number:
            print("Player 1 wins! The secret number was", secret_number)
            break
        elif player1_guess < secret_number:
            print("Too low! Player 1, try again.")
        else:
            print("Too high! Player 1, try again.")

        # Player 2's turn
        player2_guess = int(input("Player 2, enter your guess (between 1 and 20): "))
        if player2_guess == secret_number:
            print("Player 2 wins! The secret number was", secret_number)
            break
        elif player2_guess < secret_number:
            print("Too low! Player 2, try again.")
        else:
            print("Too high! Player 2, try again.")

if __name__ == "__main__":
    guess_game()
