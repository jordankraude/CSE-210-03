class Director:

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        guess = input("Guess a letter [a-z]: ")
       
    def _do_updates(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return 

    def _do_outputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        