from pygame.math import Vector2


class Rect:

    __slots__ = ('_size', '_position')
    
    def __init__(self, topleft, size):
        self._size = Vector2(size)
        self._position = Vector2(topleft)

    def collide(self, rect):
        left, top = self._position
        right, bottom = self._position + self._size

        other_left, other_top = rect._position
        other_right, other_bottom = rect._position + rect._size

        return left < other_right and right > other_left and \
               top < other_bottom and bottom > other_top

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = Vector2(value)

    @property
    def x(self):
        return self._position[0]

    @x.setter
    def x(self, value):
        self._position[0] = value

    @property
    def y(self):
        return self._position[1]

    @y.setter
    def y(self, value):
        self._position[1] = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = Vector2(value)

    @property
    def width(self):
        return self._size[0]

    @width.setter
    def width(self, value):
        self._size[0] = value

    @property
    def height(self):
        return self._size[1]

    @height.setter
    def height(self, value):
        self._size[1] = value

    @property
    def left(self):
        return self._position[0]

    @left.setter
    def left(self, value):
        self._position[0] = value

    @property
    def right(self):
        return self._position[0] + self._size[0]

    @right.setter
    def right(self, value):
        self._position[0] = value - self._size[0]

    @property
    def centerx(self):
        return self._position[0] + self._size[0] / 2

    @centerx.setter
    def centerx(self, value):
        self._position[0] = value - self._size[0] / 2

    @property
    def top(self):
        return self._position[1]

    @top.setter
    def top(self, value):
        self._position[1] = value

    @property
    def bottom(self):
        return self._position[1] + self._size[1]

    @bottom.setter
    def bottom(self, value):
        self._position[1] = value - self._size[1]

    @property
    def centery(self):
        return self._position[1] + self._size[1] // 2

    @centery.setter
    def centery(self, value):
        self._position[1] = value - self._size[1] / 2

    @property
    def topleft(self):
        return self._position

    @topleft.setter
    def topleft(self, value):
        self._position = value

    @property
    def topright(self):
        return self._position + (self._size[0], 0)

    @topright.setter
    def topright(self, value):
        self._position = Vector2(value[0] - self._size[0], value[1])

    @property
    def bottomleft(self):
        return self._position + (0, self._size[1])

    @bottomleft.setter
    def bottomleft(self, value):
        self._position = Vector2(value[0], value[1] - self._size[1])

    @property
    def bottomright(self):
        return self._position + self._size

    @bottomright.setter
    def bottomright(self, value):
        self._position = value - self._size

    @property
    def center(self):
        return self._position + self._size / 2

    @center.setter
    def center(self, value):
        self._position = Vector2(value) - self._size / 2


if __name__ == '__main__':
    a = Rect((10, 10), (32, 32))
    b = Rect((0, 0), (10, 10))
    print(a.collide(b))
    b.topleft = (42, 42)
    print(a.collide(b))
    b.topleft = (1, 1)
    print(a.collide(b))
    b.topleft = (41, 4)
    print(a.collide(b))