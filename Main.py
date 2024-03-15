import pygame
import os

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
WALL_WIDTH = SCREEN_WIDTH // 4.6
WALL_HEIGHT = SCREEN_HEIGHT // 4

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diner Flan Time!")

floor_image = pygame.image.load("./Images/Background/Floor.png").convert_alpha()
left_wall_image = pygame.image.load("./Images/Background/LeftWall.png").convert_alpha()
middle_wall_image = pygame.image.load("./Images/Background/MiddleWall.png").convert_alpha()
right_wall_image = pygame.image.load("./Images/Background/RightWall.png").convert_alpha()

left_wall_rect = pygame.Rect(0, 0, WALL_WIDTH, SCREEN_HEIGHT)
middle_wall_rect = pygame.Rect(WALL_WIDTH, 0, WALL_WIDTH, SCREEN_HEIGHT)
right_wall_rect = pygame.Rect(SCREEN_WIDTH - WALL_WIDTH, 0, WALL_WIDTH, SCREEN_HEIGHT)

left_wall_mask = pygame.mask.from_surface(left_wall_image)


character_image = pygame.image.load(os.path.join("./Images\Characters\Waitress\Waitress.png")).convert_alpha()
character_rect = character_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

character_mask= pygame.mask.from_surface(character_image)



clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        character_rect.x += 5
    if keys[pygame.K_UP]:
        character_rect.y -= 5
    if keys[pygame.K_DOWN]:
        character_rect.y += 5

    screen.fill((0, 0, 0))
    screen.blit(floor_image, (0, SCREEN_HEIGHT // 4.6))
    screen.blit(left_wall_image, (0, 0))
    screen.blit(middle_wall_image, (WALL_WIDTH, 0))
    screen.blit(right_wall_image, (SCREEN_WIDTH - WALL_WIDTH, 0))
    screen.blit(character_image, character_rect)

   # if character_mask.overlap(left_wall_image(0) - character_rect.x,left_wall_image(0) - character_rect.y )
    if character_mask.overlap(left_wall_mask, ( left_wall_rect.x - character_rect.x, left_wall_rect.y - character_rect.y )):
        print("COLISSIOOON")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
