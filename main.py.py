from random import randint

def guessGame() :
    print("-----Welcome To Guessing Game-----")
    while True:
        # Generate random number between 1 and 100
        n = randint(1, 100)
        
        guesses = 0  # Initialize number of attempts to 0
        max_attempts = 10  # Maximum number of attempts allowed
        
        while guesses < max_attempts:
            a = int(input("\nGuess The Number (between 1 and 100): "))
            guesses += 1
            
            if a < n:
                print("Higher Number Please.")
            elif a > n:
                print("Lower Number Please.")
            else:
                print("Correct Guess!")
                break  # Exit the inner loop if the guess is correct
        
        if a == n:
            print(f"Number to Guess: {n}")
            print(f"Number of Attempts: {guesses}")
        else:
            print(f"Out of Attempts! The number to guess was: {n}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break 
guessGame()