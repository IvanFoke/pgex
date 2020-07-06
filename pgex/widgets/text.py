from pygame import font, draw
from pgex.parameters.colors import colors


class Text:
    def __init__(self, text, font_path, font_size=20, font_color=colors["black"], bg_color=None, border_width=1):
        self._text = text
        self.font_size = font_size
        self.font_name = font_path
        self.font_color = font_color
        self.bg_color = bg_color
        self.border_width = border_width

    def get_rect(self):
        text = self._render_text()
        return text.get_rect()

    def _render_text(self):
        font_type = font.Font(self.font_name, self.font_size)
        text = font_type.render(self._text, True, self.font_color)
        return text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def draw(self, screen, coordinates):
        text = self._render_text()
        text_rect = text.get_rect()

        if self.bg_color:
            draw.rect(screen, self.bg_color, (coordinates[0], coordinates[1], text_rect.width, text_rect.height),
                      self.border_width)

        screen.blit(text, coordinates)
