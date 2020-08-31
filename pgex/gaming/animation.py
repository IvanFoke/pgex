# import pygame as pg


class AnimationIterator:
    def __init__(self, images, frames_per_image):
        self.images = tuple(images)
        self.fpi = frames_per_image
        self.count = 0
        self.index = 0
        self.size = len(self.images)

    def __next__(self):
        if self.count < self.fpi:
            self.count += 1
            return self.images[self.index]
        self.count = 0
        self.index += 1
        if self.index == self.size:
            self.index = 0
        return next(self)

    def __iter__(self):
        return self


class SimpleAnimation:
    def __init__(self, images, frames_per_image=1):
        self._animation_iter = AnimationIterator(images, frames_per_image)

    def draw(self, screen, coordinates):
        screen.blit(next(self._animation_iter), coordinates)

    def __str__(self):
        return f"SimpleAnimation(size: {self._animation_iter.size}, frames per image: {self._animation_iter.fpi})"


# if __name__ == "__main__":
#     i = AnimationIterator((1, 2, 3), 2)
#     for x in i:
#         print(x)
