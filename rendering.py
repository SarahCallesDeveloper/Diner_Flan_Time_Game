import pygame
from initialize import *

def render_screen(screen, floor_image, left_wall_image, middle_wall_image, right_wall_image, character, obstacles):
   
    screen.fill((0, 0, 0))
    screen.blit(floor_image, (0, SCREEN_HEIGHT // 4.6))
    screen.blit(left_wall_image, (0, 0))
    screen.blit(middle_wall_image, (WALL_WIDTH, 0))
    screen.blit(right_wall_image, (SCREEN_WIDTH - WALL_WIDTH, 0))

    character_mask_rect = character.mask.get_bounding_rects()[0]
    character_mask_rect.move_ip(character.rect.topleft[0] - character.rect.left, character.rect.topleft[1] - character.rect.top)

    for obstacle in obstacles:
        if Waitress.lower_mask_rect.bottom < obstacle.rect.bottom:
            print(f"Obstacle {obstacle.label} is on top of the character")
            screen.blit(character.image, character.rect)
            screen.blit(obstacle.image, obstacle.rect)
        else:
            print(f"Obstacle {obstacle.label} is below the character")
            screen.blit(obstacle.image, obstacle.rect)
            screen.blit(character.image, character.rect)

    pygame.display.flip()
