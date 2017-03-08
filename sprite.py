from xml.etree import ElementTree
import os
import pygame
from pygame.math import Vector2
from rect import Rect


class Sprite(Rect):

    ID = 0

    def __init__(self, image, position):
        super(Sprite, self).__init__(position, image.get_size())
        self._original_image = image
        self._image = image.copy()
        self.ID = Sprite.ID
        Sprite.ID += 1

    def rotate(self, angle, pivot='center'):
        old_pivot = getattr(self, pivot)
        self._image = pygame.transform.rotate(self._original_image, angle)
        self.size = self._image.get_size()
        setattr(self, pivot, old_pivot)

    def scale(self, size, pivot='center'):
        old_pivot = getattr(self, pivot)
        self._image = pygame.transform.scale(self._original_image, size)
        self._size = Vector2(size)
        setattr(self, pivot, old_pivot)

    def flip(self, x_axis=True, y_axis=False):
        self._image = pygame.transform.flip(self._original_image, x_axis, y_axis)

    def draw(self, surface):
        surface.blit(self._image, self)

    def update(self):
        pass

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._original_image = value
        self._image = value.copy()
        self.scale(value.get_size())

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self.scale(value)

    def __repr__(self):
        return str(self.ID)


class Projectile(Sprite):

    def __init__(self, image, position, velocity):
        super(Projectile, self).__init__(image, position)
        self.velocity = Vector2(velocity)

    def update(self):
        self.position += self.velocity


class Background:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, pygame.display.get_surface().get_size())
        self.position = Vector2(0, 0)


class ScrollingBackground:
    def __init__(self, image, velocity):
        screen_size = pygame.display.get_surface().get_size()
        image = pygame.transform.scale(image, screen_size)
        dx, dy = velocity
        x, y = 0, 0
        width, height = Vector2(screen_size) + Vector2(screen_size).elementwise() * (dx != 0, dy != 0)
        check_x = None
        check_y = None

        new_image = pygame.Surface((width, height))

        new_image.blit(image, (0, 0))
        if dx != 0:
            new_image.blit(image, (width / 2, 0))
            check_x = (lambda x: x < -width / 2) if dx < 0 else (lambda x: x > 0)
            x = 0 if dx < 0 else -width / 2
        if dy != 0:
            new_image.blit(image, (0, height / 2))
            check_y = (lambda y: y < -height / 2) if dy < 0 else (lambda y: y > 0)
            y = 0 if dy < 0 else -height / 2
        if dx != 0 and dy != 0:
            new_image.blit(image, (width / 2, height / 2))

        # If dx is negative, x is 0. If dx is positive, x is -width/2.
        # If dy is negative, y is 0. If dy is positive, y is -height/2.

        # If dx is negative, end_x is less than -width/2 . If dx is positive, end_x is greater than 0
        # If dy is negative, end_y is less than -height/2. If dy is positive, end_y is greater than 0.

        self._check_x = check_x
        self._check_y = check_y
        self._reset_position = Vector2(x, y)
        self.position = Vector2(x, y)
        self.velocity = Vector2(velocity)
        self.image = new_image

    def update(self):
        self.position += self.velocity
        x, y = self.position
        if self._check_x is not None and self._check_x(x):
            self.position[0] = self._reset_position[0]
        if self._check_y is not None and self._check_y(y):
            self.position[1] = self._reset_position[1]


def load_sprites():

    tree = ElementTree.parse('images/Spritesheet/sheet.xml')
    root = tree.getroot()

    path = root.attrib['imagePath']
    spritesheet = pygame.image.load(os.path.join(os.getcwd() + '/images/Spritesheet', path)).convert_alpha()

    images = {}
    for child in root:
        name = child.attrib['name'].replace('.png', '')
        x, y, width, height = tuple(map(int, (child.attrib['x'], child.attrib['y'], child.attrib['width'], child.attrib['height'])))
        image = spritesheet.subsurface(pygame.Rect(x, y, width, height))
        images[name] = image

    return images


