from pgex.widgets import Text
from pgex.widgets import Button
from pgex.widgets import Entry
from pgex.parameters import colors
import pygame as pg


class PgEx:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Pgex Example")

        self.clock = pg.time.Clock()
        self.game_over = False
        self.txt = Text("SomeText", r'Crushez.ttf', 100, font_color=colors["dark_gray"], bg_color=colors["white"], border_width=1)
        self.btn = Button(200, 100, "Btn", r'Crushez.ttf', 40, r'button.wav', action=self.get_entry_text, centralized=True)
        self.entry = Entry(200, 50, r'Crushez.ttf', 20, centralized=True)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.game_over = True
                return False
        return True

    def run(self):
        while not self.game_over:
            events = pg.event.get()
            if not self.handle_events(events):
                break

            self.screen.fill(colors["light_blue"])
            self.txt.draw(self.screen, (100, 300))
            self.btn.draw(self.screen, (500, 100))
            self.entry.draw(self.screen, (100, 200), events)

            pg.display.update()
            self.clock.tick(30)
        pg.quit()

    def get_entry_text(self):
        print(f"Got text: {self.entry.text}")


if __name__ == "__main__":
    PgEx().run()
