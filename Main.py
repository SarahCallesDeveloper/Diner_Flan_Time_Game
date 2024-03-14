import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
WALL_WIDTH = SCREEN_WIDTH // 4.6
WALL_HEIGHT = SCREEN_HEIGHT // 4

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diner Flan Time!")
# Load images for background
floor_image = pygame.image.load("./Images/Background/Floor.png").convert_alpha()
left_wall_image = pygame.image.load("./Images/Background/LeftWall.png").convert_alpha()
middle_wall_image = pygame.image.load("./Images/Background/MiddleWall.png").convert_alpha()
right_wall_image = pygame.image.load("./Images/Background/RightWall.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Blit floor image
    screen.blit(floor_image, (0, SCREEN_HEIGHT // 4.6))
    
    # Blit left wall image
    screen.blit(left_wall_image, (0, 0))

    # Blit middle wall image

    screen.blit(middle_wall_image, (WALL_WIDTH, 0))

    # Blit right wall image
    screen.blit(right_wall_image, (SCREEN_WIDTH - WALL_WIDTH, 0))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
