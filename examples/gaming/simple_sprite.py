from pgex.gaming import SimpleSprite
from pgex.parameters import colors
import pygame as pg


class PgEx:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Pgex Example")

        self.clock = pg.time.Clock()
        self.game_over = False

        bee_image = pg.image.load(r"bee.png").convert_alpha()
        self.bee = SimpleSprite((200, 200), 3, 3, bee_image)

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

            if self.bee.is_out_of_screen(800, 600, left=True):
                self.bee.left(800 - 1)
            elif self.bee.is_out_of_screen(800, 600, right=True):
                self.bee.right(0 + 1)

            self.bee.draw(self.screen)

            pg.display.update()
            self.clock.tick(30)
        pg.quit()


if __name__ == "__main__":
    PgEx().run()
