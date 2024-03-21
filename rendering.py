# rendering.py
import pygame
from initialize import *

def render_screen(screen, floor_image, left_wall_image, middle_wall_image, right_wall_image, lower_mask, character_rect, mushroom_table_SmallMask_rect, lower_mask_rect, SCREEN_HEIGHT):
    screen.fill((0, 0, 0))
    screen.blit(floor_image, (0, SCREEN_HEIGHT // 4.6))
    screen.blit(left_wall_image, (0, 0))
    screen.blit(middle_wall_image, (WALL_WIDTH, 0))
    screen.blit(right_wall_image, (SCREEN_WIDTH - WALL_WIDTH, 0))

    character_mask_rect = character_mask.get_bounding_rects()[0]
    character_mask_rect.move_ip(character_rect.topleft[0] - mushroom_table_SmallMask_rect.left, character_rect.topleft[1] - mushroom_table_SmallMask_rect.top)
    
    for mushroom in mushroom_tables:
        if lower_mask_rect.bottom < mushroom.rect.bottom:
            print(f"mushroom number {mushroom.label} is below character")
            screen.blit(character_image, character_rect)
            screen.blit(mushroom.image, mushroom.rect)
        else:
            screen.blit(mushroom.image, mushroom.rect)
            screen.blit(character_image, character_rect)

    pygame.display.flip()
