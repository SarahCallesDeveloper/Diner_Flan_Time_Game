# initialization.py
import pygame
import os

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
WALL_WIDTH = SCREEN_WIDTH // 4.6
WALL_HEIGHT = SCREEN_HEIGHT // 4



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diner Flan Time!")

#BORDERS
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

#MUSHROOMS
class MushroomTable:
    def __init__(self, image, center_x, center_y, label):
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect(center=(center_x, center_y))
        self.small_mask_rect = self.rect.inflate(0, -self.rect.height // 1.5)
        self.small_mask_rect.bottom = self.rect.bottom
        self.label = label

mushroom_table_image = pygame.image.load("./Images/Background/MushroomTable.png")

# instances of mushroom tables with labels
mushroom_tables = [
    MushroomTable(mushroom_table_image, SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 4, "Table 1"),
    MushroomTable(mushroom_table_image, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Table 2"),
    MushroomTable(mushroom_table_image, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, "Table 3")
]


#CHARACTER
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
lower_mask_rect = pygame.Rect(0, 0, width, lower_quarter_height)

#ARRAYS
obstacles_Array=[mushroom_tables[0].small_mask_rect]
masks_array=[middle_wall_mask]