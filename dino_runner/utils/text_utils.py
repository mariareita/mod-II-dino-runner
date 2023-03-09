import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
BLACK_COLOR = (0, 0, 0)

def get_score_element(poins):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"poins: {poins}", True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1010, 35)
    return text, text_rect

def get_home_message(message):
    font = pygame.font.Font(FONT_STYLE, 50)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (550, 300)
    return text, text_rect

def get_centered_message(message):
    font = pygame.font.Font(FONT_STYLE, 50)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (550, 300)
    return text, text_rect

def get_number_of_deaths(deaths):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"Deaths Count: {deaths}", True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (550, 350)
    return text, text_rect
