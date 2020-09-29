from pgex.gaming import AnimatedSprite
from pgex.parameters import colors
import pygame as pg


class PgEx:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Pgex Example")

        self.clock = pg.time.Clock()
        self.game_over = False

        l_images = (pg.image.load(r"bee\bee_left_0.png").convert(), pg.image.load(r"bee\bee_left_1.png").convert())
        r_images = (pg.image.load(r"bee\bee_right_0.png").convert(), pg.image.load(r"bee\bee_right_1.png").convert())
        u_images = (pg.image.load(r"bee\bee_up_0.png").convert(), pg.image.load(r"bee\bee_up_1.png").convert())
        d_images = (pg.image.load(r"bee\bee_down_0.png").convert(), pg.image.load(r"bee\bee_down_1.png").convert())

        self.bug = AnimatedSprite((178, 130), (100, 100), 3, 3, (d_images[0],), l_images, r_images, u_images, d_images,
                                  colors["black"], 3)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.game_over = True

    def run(self):
        while not self.game_over:
            events = pg.event.get()
            self.handle_events(events)

            keys = pg.key.get_pressed()

            self.screen.fill(colors["light_blue"])
            self.bug.move(self.screen, keys)

            pg.display.update()
            self.clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    PgEx().run()
