from pgex.gaming.animation import AnimationIterator
import pygame as pg


class AnimatedSprite:
    def __init__(self, size, coordinates, speed_x, speed_y, stay_images, left_images=None, right_images=None,
                 up_images=None, down_images=None, transparent_color=None, frames_per_image=1):
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

        self.jump_mul = 1
        self.jump_velocity = 5

    def stay(self, screen):
        self.surf.blit(next(self.stay_animation), (0, 0))
        screen.blit(self.surf, self.rect)

    def move_left(self, screen):
        self.rect.x -= self.speed_x
        self.surf.blit(next(self.left_animation), (0, 0))
        screen.blit(self.surf, self.rect)

    def move_right(self, screen):
        self.rect.x += self.speed_x
        self.surf.blit(next(self.right_animation), (0, 0))
        screen.blit(self.surf, self.rect)

    def move_up(self, screen):
        self.rect.y -= self.speed_y
        self.surf.blit(next(self.up_animation), (0, 0))
        screen.blit(self.surf, self.rect)

    def move_down(self, screen):
        self.rect.y += self.speed_y
        self.surf.blit(next(self.down_animation), (0, 0))
        screen.blit(self.surf, self.rect)

    def move(self, screen, keys=None):
        if keys is None:
            keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.move_left(screen)
        elif keys[pg.K_RIGHT]:
            self.move_right(screen)
        elif keys[pg.K_UP]:
            self.move_up(screen)
        elif keys[pg.K_DOWN]:
            self.move_down(screen)
        else:
            self.stay(screen)

    def jump(self):
        # TODO: add jump with sprite
        pass

    def collide_sprite(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def collide_rect(self, rect):
        return self.rect.colliderect(rect)

    def contains_sprite(self, sprite):
        return self.rect.contains(sprite.rect)

    def contains_rect(self, rect):
        return self.rect.contains(rect)

