from pgex.gaming.animation import AnimationIterator
import pygame as pg


class AnimatedSprite:
    def __init__(self, size, coordinates, speed_x, speed_y, stay_images, left_images=None, right_images=None,
                 up_images=None, down_images=None, jump_images=None, transparent_color=None, frames_per_image=1):
        self.surf = pg.Surface(size)
        if transparent_color:
            self.surf.set_colorkey(transparent_color)
        self.rect = self.surf.get_rect()
        self.rect.center = coordinates
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.stay_animation = AnimationIterator(stay_images, frames_per_image)
        self.left_animation = AnimationIterator(left_images, frames_per_image) if left_images else self.stay_animation
        self.right_animation = AnimationIterator(right_images, frames_per_image) if right_images else self.stay_animation
        self.up_animation = AnimationIterator(up_images, frames_per_image) if up_images else self.stay_animation
        self.down_animation = AnimationIterator(down_images, frames_per_image) if down_images else self.stay_animation
        self.jump_animation = AnimationIterator(jump_images, frames_per_image) if jump_images else self.stay_animation

        self.jump_multiplier = 2
        self._current_jump_mul = self.jump_multiplier
        self.jump_velocity = 5
        self.need_jump = False

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def stay(self):
        self.surf.blit(next(self.stay_animation), (0, 0))

    def move_left(self):
        self.rect.x -= self.speed_x
        self.surf.blit(next(self.left_animation), (0, 0))

    def move_right(self):
        self.rect.x += self.speed_x
        self.surf.blit(next(self.right_animation), (0, 0))

    def move_up(self):
        self.rect.y -= self.speed_y
        self.surf.blit(next(self.up_animation), (0, 0))

    def move_down(self):
        self.rect.y += self.speed_y
        self.surf.blit(next(self.down_animation), (0, 0))

    def move(self, keys=None):
        if keys is None:
            keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.move_left()
        elif keys[pg.K_RIGHT]:
            self.move_right()
        elif keys[pg.K_UP]:
            self.move_up()
        elif keys[pg.K_DOWN]:
            self.move_down()
        else:
            self.stay()

    def jump(self):
        if self.need_jump:
            force = int(0.5 * self._current_jump_mul * self.jump_velocity ** 2)
            self.rect.y -= force
            self.jump_velocity -= 1
            if self.jump_velocity < 0:
                self._current_jump_mul = -self.jump_multiplier
            if self.jump_velocity == -6:
                self.need_jump = False
                self.jump_velocity = 5
                self._current_jump_mul = self.jump_multiplier

        self.surf.blit(next(self.jump_animation), (0, 0))

    def collide_sprite(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def collide_rect(self, rect):
        return self.rect.colliderect(rect)

    def contains_sprite(self, sprite):
        return self.rect.contains(sprite.rect)

    def contains_rect(self, rect):
        return self.rect.contains(rect)

