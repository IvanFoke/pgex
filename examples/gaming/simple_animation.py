from pgex.gaming import SimpleAnimation
from pgex.parameters import colors
import pygame as pg


class PgEx:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Pgex Example")

        self.clock = pg.time.Clock()
        self.game_over = False

        images = (pg.image.load(r"bug\bug_0.png"), pg.image.load(r"bug\bug_1.png"))
        self.bug_animation = SimpleAnimation(images, (100, 100), 3)
        del images

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
            self.bug_animation.draw(self.screen)

            pg.display.update()
            self.clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    PgEx().run()
