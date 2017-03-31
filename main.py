import pygame
from pytmx.util_pygame import load_pygame


pygame.init()
screen_width = 1100
screen_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode([screen_width, screen_height])
tmx_map = load_pygame("track.tmx")
pygame.display.set_caption("Don't get caught!!!")
clock = pygame.time.Clock()

car_img = pygame.image.load('getawaycar.png')

car_width = 47


def map_game():
    for layer in tmx_map.visible_layers:
        for x, y, gid, in layer:
            tile = tmx_map.get_tile_image_by_gid(gid)
            if tile is None:
                continue
            screen.blit(tile, (x * tmx_map.tilewidth, y * tmx_map.tileheight))


def car(x_coordinate, y_coordinate):
    screen.blit(car_img, (x_coordinate, y_coordinate))


def the_game_loop():

    quitter = False
    x = (screen_width * 0.45)
    y = (screen_height * 0.7)
    x_change = 0
    y_change = 0

    while not quitter:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitter = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15

                elif event.key == pygame.K_RIGHT:
                    x_change = 15
                elif event.key == pygame.K_UP:
                    y_change = -15

                elif event.key == pygame.K_DOWN:
                    y_change = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        if x > 864 or x < 320:
            continue

        map_game()
        car(x, y)
        pygame.display.update()
        clock.tick(30)


the_game_loop()
pygame.quit()
quit()
