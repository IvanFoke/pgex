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

        self.bee = AnimatedSprite((200, 400), 3, 3, (d_images[0],), l_images, r_images, u_images, d_images,
                                  None, colors["black"], 3)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.game_over = True

    def run(self):
        while not self.game_over:
            events = pg.event.get()
            self.handle_events(events)

            self.screen.fill(colors["light_blue"])
            self.bee.move(up=False, down=False)

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.bee.need_jump = True
            if self.bee.need_jump:
                self.bee.jump()

            if self.bee.right() < 0:
                self.bee.left(800)

            self.bee.draw(self.screen)

            pg.display.update()
            self.clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    PgEx().run()
