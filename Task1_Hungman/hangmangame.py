import random

# 5 predefined words
words = ["python", "computer", "program", "coding", "developer", "random", "data", "particular", "store", "dynamic", "cricket", "chess", "ludoking"]

# Choose a random word
word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 5

print("=" * 45)
print("          🎮 HANGMAN GAME")
print("=" * 45)
print("Guess the hidden word one letter at a time.")
print("You can make only 5 wrong guesses.")
print("=" * 45)

while wrong_guesses < max_wrong_guesses:

    # Display current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check whether the complete word is guessed
    if all(letter in guessed_letters for letter in word):
        print("\n Congratulations...🎉")
        print("You guessed the word:", word)
        print(" You won the game!..🏆")
        break

    # Take input
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one alphabet.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the letter is correct
    if guess in word:
        print("✅ Correct guess!")

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

        remaining = max_wrong_guesses - wrong_guesses
        print("Chances remaining:", remaining)

# If player uses all chances
if wrong_guesses == max_wrong_guesses:
    print("\n" + "=" * 45)
    print("              ☠️  GAME OVER ☠️")
    print("=" * 45)
    print("The correct word was:", word)
    print("Better luck for next time...😊")
    print("Thank you for playing the game! Hope you enjoyed it.😊")
