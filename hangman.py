import random

words = ["python", "hangman", "program", "developer", "internship"]
word_to_guess = random.choice(words)

guessed_letters = set()
incorrect_guesses = 0
max_incorrect_guesses = 6

print("🎯 Welcome to Hangman!")
print(f"The word has {len(word_to_guess)} letters.\n")

while incorrect_guesses < max_incorrect_guesses:
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
    print(display_word)

    if "_" not in display_word:
        print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("🔄 You already guessed that letter.\n")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Incorrect guess. Attempts left: {max_incorrect_guesses - incorrect_guesses}\n")

if incorrect_guesses == max_incorrect_guesses:
    print(f"😞 You lost! The word was: {word_to_guess}")
