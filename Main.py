import pygame
from initialize import *
from event_handler import *
from rendering import *

pygame.init()

clock = pygame.time.Clock()
movement_value = 5
running = True
while running:
    # Event Handling
    result = handle_events(character_rect, character_mask, lower_quarter_height, movement_value, obstacles_Array, masks_array)
    if not result:
        running = False
    else:
        character_rect, lower_mask_rect = result

    # Rendering
    render_screen(screen, floor_image, left_wall_image, middle_wall_image, right_wall_image, lower_mask, character_rect, mushroom_tables[0].rect, lower_mask_rect, SCREEN_HEIGHT)

    clock.tick(60)

pygame.quit()
 