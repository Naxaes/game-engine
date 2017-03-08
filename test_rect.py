from timeit import timeit


def test_rect():
    from rect import Rect as MyRect
    from pygame import Rect as PyRect

    rect1 = MyRect((20, 20), (32, 32))
    rect2 = PyRect((20, 20), (32, 32))

    def move_single(rect):
        rect.right = 100

    def move_double(rect):
        rect.bottomleft = (100, 400)

    def scale(rect):
        rect.size = (200, 200)

    number = 1000000

    print('Create: ')
    print(timeit(lambda: MyRect((20, 20), (32, 32)), number=number) / number)
    print(timeit(lambda: PyRect((20, 20), (32, 32)), number=number) / number)

    print('\nMove single dimension: ')
    print(timeit(lambda: move_single(rect1), number=number) / number)
    print(timeit(lambda: move_single(rect2), number=number) / number)

    print('\nMove double dimension: ')
    print(timeit(lambda: move_double(rect1), number=number) / number)
    print(timeit(lambda: move_double(rect2), number=number) / number)

    print('\nScale: ')
    print(timeit(lambda: scale(rect1), number=number) / number)
    print(timeit(lambda: scale(rect2), number=number) / number)


def test_sprite_group():
    import pygame
    from groups import SpriteGroup, SpriteGroup2, SpriteGroup3
    from sprite import Sprite

    group1 = SpriteGroup()
    group2 = SpriteGroup2()
    group3 = SpriteGroup3()

    surface = pygame.Surface((32, 32))
    sprites = [Sprite(surface, (0, 0)) for _ in range(100000)]

    def update(group):
        group.update()

    def draw(group):
        group.draw(surface)

    def add(group):
        group.add(*sprites)

    def remove(group):
        group.remove(*[sprite for index, sprite in enumerate(sprites) if index % 5 == 0])

    def clear(group):
        group.clear()

    number = 1

    print('Create: ')
    print('{:.4E}'.format(timeit(lambda: SpriteGroup(), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: SpriteGroup2(), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: SpriteGroup3(), number=number) / number))

    print('\nCreate with sprites: ')
    print('{:.4E}'.format(timeit(lambda: SpriteGroup(*sprites), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: SpriteGroup2(*sprites), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: SpriteGroup3(*sprites), number=number) / number))

    print('\nAdd: ')
    print('{:.4E}'.format(timeit(lambda: add(group1), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: add(group2), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: add(group3), number=number) / number))

    print('\nRemove: ')
    print('{:.4E}'.format(timeit(lambda: remove(group1), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: remove(group2), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: remove(group3), number=number) / number))

    print('\nAdd: ')
    print('{:.4E}'.format(timeit(lambda: add(group1), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: add(group2), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: add(group3), number=number) / number))

    print('\nDraw: ')
    print('{:.4E}'.format(timeit(lambda: draw(group1), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: draw(group2), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: draw(group3), number=number) / number))

    print('\nUpdate: ')
    print('{:.4E}'.format(timeit(lambda: update(group1), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: update(group2), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: update(group3), number=number) / number))

    print('\nClear: ')
    print('{:.4E}'.format(timeit(lambda: clear(group1), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: clear(group2), number=number) / number))
    print('{:.4E}'.format(timeit(lambda: clear(group3), number=number) / number))


if __name__ == '__main__':
    test_sprite_group()
    # import pygame
    # from sprite import SpriteGroup2, Sprite
    # surface = pygame.Surface((32, 32))
    # sprites = [Sprite(surface, (3, 3)) for _ in range(10)]
    # a = SpriteGroup2(*sprites)
    # print(len(a))
    # print(a)
    # a.remove(*sprites[3:5], sprites[9], sprites[0])
    # print(len(a))
    # print(a)
    # a.remove(sprites[2])
    # print(len(a))
    # print(a)