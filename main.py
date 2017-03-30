import pygame


pygame.init()
screen_width = 1100
screen_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Don't get caught!!!")
clock = pygame.time.Clock()

car_img = pygame.image.load('getawaycar.png')
car_width = 47


def car(x_coordinate, y_coordinate):
    screen.blit(car_img, (x_coordinate, y_coordinate))


def the_game_loop():
    global car_width
    quitter = False
    x = (screen_width * 0.45)
    y = (screen_height * 0.7)

    x_change = 0

    while not quitter:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitter = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -10

                    if x < 0:
                        x_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = 10

                    if x > (screen_width - car_width):
                        x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill(white)
        car(x, y)
        pygame.display.update()
        clock.tick(90)


the_game_loop()
pygame.quit()
quit()
