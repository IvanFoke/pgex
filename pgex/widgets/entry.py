from pgex.widgets.text import Text
from pgex.parameters.colors import colors
import pygame as pg


class Entry:
    def __init__(self, width, height, text, font_path, font_size=20, font_color=colors["black"], centralized=False):
        self.width = width
        self.height = height
        self._text = Text(text, font_path, font_size, font_color)
        self.entering_text = False
        self.x = 0
        self.y = 0
        self.input_rect = pg.Rect(0, 0, self.width, self.height)
        self.centralized = centralized

    def draw(self, screen, coordinates, pg_events):
        if self.entering_text:
            self._get_input(screen, coordinates, pg_events)
            return
        x, y = coordinates
        mouse_pos, mouse_click = pg.mouse.get_pos(), pg.mouse.get_pressed()
        if (self.x, self.y) != coordinates:
            self.input_rect = pg.Rect(x, y, self.width, self.height)
        text_coordinates = coordinates
        if self.centralized:
            text_rect = self._text.get_rect()
            text_coordinates = (x + self.width // 2 - text_rect.width // 2,
                                y + self.height // 2 - text_rect.height // 2)

        if self.input_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if mouse_click[0]:
                self.entering_text = True
                self._get_input(screen, coordinates, pg_events)
            else:
                pg.draw.rect(screen, colors["white"], self.input_rect)
                pg.draw.rect(screen, colors["black"], (x, y, self.width, self.height), 3)
                self._text.draw(screen, text_coordinates)
        else:
            pg.draw.rect(screen, colors["white"], self.input_rect)
            pg.draw.rect(screen, colors["black"], (x, y, self.width, self.height), 1)
            self._text.draw(screen, text_coordinates)

    def _get_input(self, screen, coordinates, pg_events):
        x, y = coordinates
        text_coordinates = coordinates
        if self.centralized:
            text_rect = self._text.get_rect()
            text_coordinates = (x + self.width // 2 - text_rect.width // 2,
                                y + self.height // 2 - text_rect.height // 2)

        pg.draw.rect(screen, colors["white"], self.input_rect)
        pg.draw.rect(screen, colors["black"], (x, y, self.width, self.height), 3)
        self._text.draw(screen, text_coordinates)

        for event in pg_events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_ESCAPE:
                    self.entering_text = False
                    return
                elif event.key == pg.K_BACKSPACE:
                    self._text.text = self._text.text[:-1]
                elif event.unicode.isascii():
                    self._text.text = self._text.text + event.unicode
                    text_rect = self._text.get_rect()
                    if text_rect.width >= self.input_rect.width:
                        self._text.text = self._text.text[:-1]

        mouse_pos, mouse_click = pg.mouse.get_pos(), pg.mouse.get_pressed()
        if not self.input_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and mouse_click[0]:
            self.entering_text = False

    @property
    def text(self):
        return self._text.text

    @text.setter
    def text(self, text):
        self._text.text = text
