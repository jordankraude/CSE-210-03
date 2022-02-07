from word_class import Word

class Director:

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._word = Word()

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

        failed = 0
        for char in word_final:
            if char in guesses:
                print(f'{char}')
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("Congratulations! You Won!")

        if letter not in word_final:
            turns -= 1
            print('Wrong!')
            print(f'You have {turns} more guesses')

    def _do_outputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        