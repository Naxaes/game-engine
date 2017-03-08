class SpriteGroup:

    def __init__(self, *sprites):
        self.sprites = list(sprites)

    def add(self, *sprites):
        self.sprites.extend(sprites)

    def draw(self, surface):
        for sprite in self.sprites:
            surface.blit(sprite.image, sprite.position)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def remove(self, *sprites):
        for sprite in sprites:
            try:
                self.sprites.remove(sprite)
            except ValueError:
                pass

    def clear(self):
        self.sprites = []


class SpriteGroup2:

    __slots__ = ('_first', '_last')

    class Node:

        __slots__ = ('data', 'next')

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_

    def __init__(self, *sprites):
        self._first = self._last = None
        if sprites:
            self.add(*sprites)

    def add(self, *sprites):
        sprites = iter(sprites)
        Node = SpriteGroup2.Node

        new = Node(next(sprites))
        if self.is_empty():
            self._last = self._first = new
        else:
            self._last.next = new
            self._last = new

        for sprite in sprites:
            new = Node(sprite)
            self._last.next = new
            self._last = new

    def is_empty(self):
        return self._first is None

    def draw(self, surface):
        node = self._first
        while node is not None:
            sprite = node.data
            surface.blit(sprite.image, sprite.position)
            node = node.next

    def update(self):
        node = self._first
        while node is not None:
            sprite = node.data
            sprite.update()
            node = node.next

    def remove(self, *sprites):
        sprites = list(sprites)  # Should be linked list.
        node = self._first
        previous = None
        while node is not None:
            if node.data in sprites:
                if previous is not None:
                    previous.next = node.next
                else:
                    self._first = node.next
                sprites.remove(node.data)
            else:
                previous = node
            node = node.next

    def clear(self):
        self._first = self._last = None

    def __len__(self):
        length = 0
        node = self._first
        while node is not None:
            length += 1
            node = node.next
        return length

    def __str__(self):
        a = ''
        node = self._first
        while node is not None:
            a += str(node.ID) + ' '
            node = node.next
        return a


class SpriteGroup3:

    __slots__ = ('_first', '_last')

    def __init__(self, *sprites):
        self._first = self._last = None
        if sprites:
            self.add(*sprites)

    def add(self, *sprites):
        sprites = iter(sprites)

        new = next(sprites)
        if self.is_empty():
            self._last = self._first = new
            new.__next = None
            new.__previous = None
        else:
            new.__previous = self._last
            self._last.__next = new
            self._last = new

        for sprite in sprites:
            sprite.__previous = self._last
            sprite.__next = None
            self._last.__next = sprite
            self._last = sprite

    def is_empty(self):
        return self._first is None

    def draw(self, surface):
        sprite = self._first
        while sprite is not None:
            surface.blit(sprite.image, sprite.position)
            sprite = sprite.__next

    def update(self):
        sprite = self._first
        while sprite is not None:
            sprite.update()
            sprite = sprite.__next

    def remove(self, *sprites):
        for sprite in sprites:
            previous = sprite.__previous
            next_ = sprite.__next

            if previous is not None:
                previous.__next = next_
            else:
                self._first = next_
            if next_ is not None:
                next_.__previous = previous
            else:
                self._last = previous

    def clear(self):
        self._first = self._last = None

    def __len__(self):
        length = 0
        sprite = self._first
        while sprite is not None:
            length += 1
            sprite = sprite.__next
        return length

