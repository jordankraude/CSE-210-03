import random
import time

class Word:
    def __init__(self) -> None:
        with open("wordlist.txt") as word_list:
            self._list = word_list.readlines()
        
        self._guesses = []

    def _getword(self):
        self._word = random.choice(self._list)
        self._word_final = self._word.replace('\n', '')
        self._word_as_list = []
        for char in self._word_final:
            char.append(self._word_as_list)

        return self._word_as_list


    ##def _updateDisplay(self, letter_guess):
    ##char = letter_guess
    ##    letters_left = 0
    ##    for char in self.word_final:
      ##      if char in self.guesses:
       ##         print(f'{char}')
         ##   else:
           ##     letters_left += 1
        
       ## if letters_left == 0:
         ##   print("Congratulations! You Won!")

