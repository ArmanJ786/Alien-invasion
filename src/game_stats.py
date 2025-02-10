class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # Credits state.
        self.credits_active = False

        self.ships_left = 0
        self.score = 0
        self.high_score = 0
        
        self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

    def load_high_score(self):
        try:
            with open('high_score.dat', 'r') as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def save_high_score(self):
        with open('high_score.dat', 'w') as f:
            f.write(str(self.high_score))
