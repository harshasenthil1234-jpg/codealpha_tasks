import random

# List of predefined words
words = ["falcon", "aardvark", "zorse", "monkey", "octopus"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== Welcome to Hangman ===")
while wrong_guesses < max_wrong:
# Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue
    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)


    # Display the word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed the word
    if "_" not in display:
        print(" Congratulations! You guessed the word:", word)
        break

    
    # Check guess
    if guess in word:
        print(" Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_wrong - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong:
    print("\n Game Over!")
    print("The word was:", word)
