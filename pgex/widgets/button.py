from pgex.widgets.text import Text
from pygame import draw, mouse, mixer, time
from pgex.parameters.colors import colors


class Button:
    def __init__(self, width, height, text, font_path, font_size, sound_path=None, font_color=colors["black"],
                 inactive_bg=colors["dark_green"], active_bg=colors["green"], pressed_bg=colors["light_green"],
                 action=lambda: None):
        self.width = width
        self.height = height
        self.text = Text(text, font_path, font_size, font_color)
        self.action = action
        self.inactive_bg = inactive_bg
        self.active_bg = active_bg
        self.pressed_bg = pressed_bg
        self.sound = mixer.Sound(sound_path) if sound_path else None

    def draw(self, screen, coordinates):
        x, y = coordinates
        mouse_pos, mouse_click = mouse.get_pos(), mouse.get_pressed()
        text_rect = self.text.get_rect()
        center = (x + self.width // 2 - text_rect.width // 2, y + self.height // 2 - text_rect.height // 2)

        if x <= mouse_pos[0] <= x + self.width and y <= mouse_pos[1] <= y + self.height:
            if mouse_click[0]:
                if self.sound:
                    self.sound.play()
                draw.rect(screen, self.pressed_bg, (x, y, self.width, self.height))
                self.text.draw(screen, center)
                self.action()

                time.delay(100)
            else:
                draw.rect(screen, self.active_bg, (x, y, self.width, self.height))
                self.text.draw(screen, center)
        else:
            draw.rect(screen, self.inactive_bg, (x, y, self.width, self.height))
            self.text.draw(screen, center)
