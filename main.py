import random
import pygame; pygame.init()
from sprite import load_sprites, SpriteGroup, Projectile, Sprite, ScrollingBackground


SIZE = WIDTH, HEIGHT = 720, 480
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

IMAGES = load_sprites()
background_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/Backgrounds/background.png'), (HEIGHT, WIDTH)), 90)

background = ScrollingBackground(background_image, velocity=(0, 1))

player = Sprite(IMAGES['playerShip1_orange'], (WIDTH//2, HEIGHT - 100))
player_speed = 2.5
player_reload_time = 0.4

enemy = Projectile(pygame.transform.flip(IMAGES['playerShip3_red'], False, True), position=(WIDTH // 2, -100), velocity=(0, 2))
enemy_respawn = 5


all_sprites = SpriteGroup(background, player, enemy)
bullets = SpriteGroup()

running = True
while running:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                player.size = (5, 5)
            elif event.key == pygame.K_n:
                player.size = (99, 75)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= player_speed
    elif keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_w]:
        player.y -= player_speed
    elif keys[pygame.K_s]:
        player.y += player_speed
    if keys[pygame.K_SPACE] and player_reload_time < 0:
        bullet_left = Projectile(IMAGES['laserRed01'], position=(player.topleft + (1, 0)), velocity=(0, -6))
        bullet_right = Projectile(IMAGES['laserRed01'], position=(player.topright - (12, 0)), velocity=(0, -6))
        bullets.add(bullet_left, bullet_right)
        all_sprites.add(bullet_left, bullet_right)
        player_reload_time = 0.4

    if enemy_respawn < 0:
        enemy.position = random.choice(list(range(96, WIDTH, 96))), -100
        enemy_respawn = 5

    for bullet in bullets.sprites:
        if enemy.collide(bullet):
            enemy.position = random.choice(list(range(96, WIDTH - 96, 96))), -100
            enemy_respawn = 5
            all_sprites.remove(bullet)
            bullets.remove(bullet)

    player_reload_time -= dt
    enemy_respawn -= dt

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
