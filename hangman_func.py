import random

def choose_word(word_list):
    return random.choice(word_list)

def display_state(underscores, guessed_list, guess_left):
    print(f'The word: {underscores}')
    print(f'Wrong Guesses: {", ".join(guessed_list)}')
    print(f'Guesses left: {guess_left}')

def get_guess(guessed_list):
    while True:
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input. Please enter a single alphabetical character.')
        elif guess in guessed_list:
            print('You have already guessed that letter.')
        else:
            return guess

def update_game_state(selected_word, list_selected_word, list_underscores, guess, guessed_list, guess_left):
    if guess in selected_word:
        for i in range(len(selected_word)):
            if list_selected_word[i] == guess:
                list_underscores[i] = guess
        underscores = ''.join(list_underscores)
    else:
        guessed_list.append(guess)
        guess_left -= 1
        underscores = ''.join(list_underscores)
    return underscores, guessed_list, guess_left

def hangman(word_list):
    selected_word = choose_word(word_list)
    list_selected_word = list(selected_word)
    underscores = ''.join(['_' for _ in selected_word])
    list_underscores = list(underscores)
    guessed_list = []
    guess_left = 6

    while guess_left > 0 and selected_word != underscores:
        display_state(underscores, guessed_list, guess_left)
        guess = get_guess(guessed_list)
        underscores, guessed_list, guess_left = update_game_state(selected_word, list_selected_word, list_underscores, guess, guessed_list, guess_left)

        if selected_word == underscores:
            print(f'Congratulations! You guessed the word: {selected_word}')
            return
    print(f'Sorry, you lost. The word was: {selected_word}')

word_list = ['apple', 'orange', 'lemon', 'watermelon', 'banana']

if __name__ == '__main__':
    hangman(word_list)
