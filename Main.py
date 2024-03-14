import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
WALL_WIDTH = SCREEN_WIDTH // 6
WALL_HEIGHT = SCREEN_HEIGHT // 4

DEFAULT_WALL_COLOR = (100, 100, 100)
FLOOR_COLOR = (50, 50, 50)
WALL_LEFT_COLOR = (255, 0, 0)
WALL_MIDDLE_COLOR = (0, 255, 0)
WALL_RIGHT_COLOR = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diner Flan Time!")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, FLOOR_COLOR, [(0, SCREEN_HEIGHT), (0, SCREEN_HEIGHT // 4), 
                                              (SCREEN_WIDTH, SCREEN_HEIGHT // 4), (SCREEN_WIDTH, SCREEN_HEIGHT)])

    pygame.draw.polygon(screen, WALL_LEFT_COLOR, [(0, SCREEN_HEIGHT), (WALL_WIDTH, SCREEN_HEIGHT // 4), 
                                                   (WALL_WIDTH, 0), (0, 0)])

    pygame.draw.rect(screen, WALL_MIDDLE_COLOR, (WALL_WIDTH, 0, SCREEN_WIDTH - 2 * WALL_WIDTH, WALL_HEIGHT))

    pygame.draw.polygon(screen, WALL_RIGHT_COLOR, [(SCREEN_WIDTH, SCREEN_HEIGHT), 
                                                   (SCREEN_WIDTH - WALL_WIDTH, SCREEN_HEIGHT // 4), 
                                                   (SCREEN_WIDTH - WALL_WIDTH, 0), 
                                                   (SCREEN_WIDTH, 0)])

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
