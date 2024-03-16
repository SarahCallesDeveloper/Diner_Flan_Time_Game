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
middle_wall_mask = pygame.mask.from_surface(middle_wall_image)
right_wall_mask = pygame.mask.from_surface(right_wall_image)


character_image = pygame.image.load(os.path.join("./Images\Characters\Waitress\Waitress.png")).convert_alpha()
character_rect = character_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Create a mask from the character image
character_mask = pygame.mask.from_surface(character_image)
width, height = character_image.get_size()

# Calculate the dimensions for the lower half
lower_half_height = height // 2

# Create a new mask for the lower half
lower_mask = pygame.mask.Mask((width, lower_half_height))

# Copy the lower half of the original mask to the new mask
for x in range(width):
    for y in range(lower_half_height):
        lower_mask.set_at((x, y), character_mask.get_at((x, y + lower_half_height)))

# Convert the lower mask to a surface
lower_mask_surface = lower_mask.to_surface()
# Create a rectangle for the lower mask surface
lower_mask_rect = pygame.Rect(0, 0, width, lower_half_height)




move_left=5
move_up=5
move_right=5
move_down=5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= move_left
    if keys[pygame.K_RIGHT]:
        character_rect.x += move_right
    if keys[pygame.K_UP]:
        character_rect.y -= move_up
    if keys[pygame.K_DOWN]:
        character_rect.y += move_down

    lower_mask_rect.topleft = character_rect.left, character_rect.bottom - lower_half_height

    screen.fill((0, 0, 0))
    screen.blit(floor_image, (0, SCREEN_HEIGHT // 4.6))
    screen.blit(left_wall_image, (0, 0))
    screen.blit(middle_wall_image, (WALL_WIDTH, 0))
    screen.blit(right_wall_image, (SCREEN_WIDTH - WALL_WIDTH, 0))
    screen.blit(character_image, character_rect)
    #screen.blit(lower_mask_surface ,lower_mask_rect)

   # if character_mask.overlap(left_wall_image(0) - character_rect.x,left_wall_image(0) - character_rect.y )
    
    if lower_mask.overlap(middle_wall_mask, ( middle_wall_rect.x - lower_mask_rect.x, middle_wall_rect.y - lower_mask_rect.y )):
        move_up=0
    else:
        move_up =5

    if lower_mask.overlap(left_wall_mask, ( left_wall_rect.x - lower_mask_rect.x, left_wall_rect.y - lower_mask_rect.y )):
        move_left = move_up = 0
    else:
        move_left  =5


    if lower_mask.overlap(right_wall_mask, ( right_wall_rect.x - lower_mask_rect.x, right_wall_rect.y - lower_mask_rect.y )):
        move_right = move_up = 0
    else:
        move_right  =5

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
