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

mushroom_table_Image_ = pygame.image.load("./Images/Background/MushroomTable.png")
mushroom_table_mask = pygame.mask.from_surface(mushroom_table_Image_)
mushroom_table_rect = mushroom_table_Image_.get_rect(center=(SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 4))
mushroom_table_SmallMask_rect = mushroom_table_rect.inflate(0, -mushroom_table_rect.height // 1.5)
mushroom_table_SmallMask_rect.bottom = mushroom_table_rect.bottom

small_mask_surface = pygame.Surface((mushroom_table_SmallMask_rect.width, mushroom_table_SmallMask_rect.height))


character_image = pygame.image.load(os.path.join("./Images\Characters\Waitress\Waitress.png")).convert_alpha()
character_rect = character_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


character_mask = pygame.mask.from_surface(character_image)
width, height = character_image.get_size()

lower_quarter_height = height // 4

lower_mask = pygame.mask.Mask((width, lower_quarter_height))

# Copy the lower quarter of the original mask to the new mask
for x in range(width):
    for y in range(lower_quarter_height):
        lower_mask.set_at((x, y), character_mask.get_at((x, y + 3 * lower_quarter_height)))

lower_mask_surface = lower_mask.to_surface()
# Create a rectangle for the lower mask surface
lower_mask_rect = pygame.Rect(0, 0, width, lower_quarter_height)

def update_image_layer(character_mask, character_rect, mushroom_table_SmallMask_rect, lower_mask_rect):
    # Get the bounding rectangle of the character mask relative to the mushroom table
    character_mask_rect = character_mask.get_bounding_rects()[0]
    character_mask_rect.move_ip(character_rect.topleft[0] - mushroom_table_SmallMask_rect.left, character_rect.topleft[1] - mushroom_table_SmallMask_rect.top)
    
    # Check if the character is below the mushroom
    if lower_mask_rect.bottom < mushroom_table_SmallMask_rect.bottom:
        screen.blit(character_image, character_rect)
        screen.blit(mushroom_table_Image_, mushroom_table_rect)
    else:
        screen.blit(mushroom_table_Image_, mushroom_table_rect)
        screen.blit(character_image, character_rect)

def move_character(character_rect, direction, movement_value):
    if direction == 'left':
        character_rect.x -= movement_value
    elif direction == 'right':
        character_rect.x += movement_value
    elif direction == 'up':
        character_rect.y -= movement_value
    elif direction == 'down':
        character_rect.y += movement_value


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    movement_value = 5
    if keys[pygame.K_LEFT]:
        move_character(character_rect, 'left', movement_value)
    if keys[pygame.K_RIGHT]:
        move_character(character_rect, 'right', movement_value)
    if keys[pygame.K_UP]:
        move_character(character_rect, 'up', movement_value)
    if keys[pygame.K_DOWN]:
        move_character(character_rect, 'down', movement_value)

    lower_mask_rect.topleft = character_rect.left, character_rect.bottom - lower_quarter_height

    screen.fill((0, 0, 0))
    screen.blit(floor_image, (0, SCREEN_HEIGHT // 4.6))
    screen.blit(left_wall_image, (0, 0))
    screen.blit(middle_wall_image, (WALL_WIDTH, 0))
    screen.blit(right_wall_image, (SCREEN_WIDTH - WALL_WIDTH, 0))
    update_image_layer(lower_mask,character_rect, mushroom_table_SmallMask_rect,lower_mask_rect)
 
   
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
