import random
import hangman_words
import hangman_art
import os

word_list = hangman_words.word_list
stages = hangman_art.stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word and guess in display:
        print(f"you already guess {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      # for windows platfrom
      _ = os.system('cls')
      
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])