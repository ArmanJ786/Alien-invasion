import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize score keeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # # Font settings for scoring information.
        self.text_color = (0, 180, 0)
        self.font = pygame.font.Font("data/assets/fonts/sevenSegment.ttf", 48)  

        # Prepare the initial score & high score image.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score).zfill(4)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 85

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = str(self.stats.high_score).zfill(4)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        
        # Display high score at top left
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        # Draw semi-transparent background for scores
        self._draw_background(self.score_rect)
        self._draw_background(self.high_score_rect)
        
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def _draw_background(self, text_rect):
        """Draw semi-transparent background behind score text."""
        bg_rect = text_rect.inflate(20, 20)  # Add padding around text
        bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 128))  # Semi-transparent black
        self.screen.blit(bg_surface, bg_rect)
