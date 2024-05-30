import random

class Hangman:
    player_list = []
    def __init__(self, word_list):
        self.word_list = word_list
        self.selected_word = self.choose_word()
        self.list_selected_word = list(self.selected_word)
        self.underscores = ['_' for _ in self.selected_word]
        self.guessed_list = []
        self.guess_left = 6
        
    def choose_word(self):
        return random.choice(self.word_list)
    
    def display_state(self):
        print(f'The word: {" ".join(self.underscores)}')
        print(f'Wrong Guesses: {", ".join(self.guessed_list)}')
        print(f'Guesses left: {self.guess_left}')
        
    def get_guess(self):
        while True:
            guess = input('Enter a letter: ').lower()
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid input. Please enter a single alphabetical character.')
            elif guess in self.guessed_list:
                print('You have already guessed that letter.')
            else:
                return guess
            
    def update_game_state(self, guess):
        if guess in self.selected_word:
            for i in range(len(self.selected_word)):
                if self.list_selected_word[i] == guess:
                    self.underscores[i] = guess
        else:
            self.guessed_list.append(guess)
            self.guess_left -= 1
    
    def check_win_loss(self):
        if '_' not in self.underscores:
            return 'win'
        elif self.guess_left <= 0:
            return 'lose'
        else:
            return 'continue'
    
    def play(self):
        while True:
            self.display_state()
            guess = self.get_guess()
            self.update_game_state(guess)
            result = self.check_win_loss()
            
            if result == 'win':
                print(f'Congratulations! You guessed the word: {self.selected_word}')
                break
            elif result == 'lose':
                print(f'Sorry, you lost. The word was: {self.selected_word}')
                break

word_list = ['apple', 'orange', 'lemon', 'watermelon', 'banana']

if __name__ == '__main__':
    game = Hangman(word_list)
    game.play()
