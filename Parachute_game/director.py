from word_class import Word
from person import Person
from parachute import Parachute
from display import Display


class Director:

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._word_list = Word()
        self._word = self._word_list._getword()
        self._person = Person()
        self._display = Display()
        self._parachute = Parachute()
        print(self._word)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            letter = self._get_inputs()
            self._do_updates(letter)
            self._do_outputs()

    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        valid = False
        while not valid:
            guess = input("Guess a letter [a-z]: ").lower()
            if len(guess) > 1:
                valid = False
                print("Please make sure the guess is only '1' letter!")
            elif len(guess) == 0:
                valid = False
                print("Please make sure the guess is only '1' letter!")
            else:
                # guesses += guess
                valid = True
                return guess
       
    def _do_updates(self, letter):
        """

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return

        if letter in self._word:
            pass
        else:
            self._parachute.break_chute()

    def _do_outputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        for i in self._parachute.parachute:
            print(i)
        print(self._person.head)
        print(self._person.body)
        print(self._person.legs)
        failed = 0
        for char in self._word:
            if char in self._word:
                print(f'{char}')
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("Congratulations! You Won!")

Director().start_game()