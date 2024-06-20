import pygame
import pygame.freetype

class PlaytimeDisplay:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.SysFont(None, 34)
        self.font.origin = True
        self.ticks = pygame.time.get_ticks()

    def run(self, playtime):
        seconds = int((playtime / 1000) % 60)
        minutes = int((playtime / 60000) % 60)
        hours = int((playtime / 3600000) % 24)
        out = '{hours:02d}:{minutes:02d}:{seconds:02d}'.format(hours=hours, minutes=minutes, seconds=seconds)
        self.font.render_to(self.window, (80, 630), out, pygame.Color('black'))
        # pygame.display.flip()
