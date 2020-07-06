from pgex.widgets.text import Text
from pygame import draw, mouse, mixer, time, Rect
from pgex.parameters.colors import colors


class Button:
    def __init__(self, width, height, text, font_path, font_size, sound_path=None, font_color=colors["black"],
                 inactive_bg=colors["dark_green"], active_bg=colors["green"], pressed_bg=colors["light_green"],
                 action=lambda: None, centralized=False):
        self.width = width
        self.height = height
        self.text = Text(text, font_path, font_size, font_color)
        self.action = action
        self.inactive_bg = inactive_bg
        self.active_bg = active_bg
        self.pressed_bg = pressed_bg
        self.sound = mixer.Sound(sound_path) if sound_path else None
        self.centralized = centralized

    def draw(self, screen, coordinates):
        x, y = coordinates
        mouse_pos, mouse_click = mouse.get_pos(), mouse.get_pressed()
        # text_rect = self.text.get_rect()
        button_rect = Rect(x, y, self.width, self.height)

        text_coordinates = coordinates
        if self.centralized:
            text_rect = self.text.get_rect()
            text_coordinates = (x + self.width // 2 - text_rect.width // 2,
                                y + self.height // 2 - text_rect.height // 2)

        # center = (x + self.width // 2 - text_rect.width // 2, y + self.height // 2 - text_rect.height // 2)

        if button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if mouse_click[0]:
                if self.sound:
                    self.sound.play()
                draw.rect(screen, self.pressed_bg, button_rect)
                self.text.draw(screen, text_coordinates)

                self.action()
                time.delay(200)
            else:
                draw.rect(screen, self.active_bg, button_rect)
                self.text.draw(screen, text_coordinates)
        else:
            draw.rect(screen, self.inactive_bg, button_rect)
            self.text.draw(screen, text_coordinates)
