import random

# Step 1: List of words
words = ["apple", "banana", "table", "chair"]

# Step 2: Randomly choose a word
word = random.choice(words)
word_letters = list(word)

# Step 3: Create a list to show guessed letters and blanks
display = ['_' for _ in word]

# Step 4: Set number of lives
lives = 6

# Step 5: Store guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter.\n")

# Step 6: Game loop
while lives > 0 and '_' in display:
    print(f"\nWord: {' '.join(display)}")
    print(f"Lives left: {lives}")
    guess = input("Enter a letter: ").lower()

    # check if input is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    # check if already guessed
    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # check if guess is in the word
    if guess in word_letters:
        print(f" Good guess! '{guess}' is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print(f" Wrong guess! '{guess}' is not in the word.")
        lives -= 1

# Step 7: Win or Lose result
if '_' not in display:
    print(f"\n Congratulations! You guessed the word: {''.join(display)}")
else:
    print(f"\n Game over! The word was: {word}")
