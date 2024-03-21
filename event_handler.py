# event_handling.py
import pygame
from initialize import * 
def check_collision(lower_mask_rect, obstacle_rect):
    return lower_mask_rect.colliderect(obstacle_rect)

def check_collision_masks(mask_rect, mask):
    return lower_mask.overlap(right_wall_mask, (right_wall_rect.x - lower_mask_rect.x, right_wall_rect.y - lower_mask_rect.y))

def move_character(character_rect, character_mask, direction, movement_value, obstacles, mask_array):
    new_rect = character_rect.copy()

    if direction == 'left':
        new_rect.x -= movement_value
    elif direction == 'right':
        new_rect.x += movement_value
    elif direction == 'up':
        new_rect.y -= movement_value
    elif direction == 'down':
        new_rect.y += movement_value

    # Check collision with obstacles(rects)
    for obstacle_rect in obstacles:
        lower_mask_rect = pygame.Rect(new_rect.left, new_rect.bottom - character_rect.height // 4, character_rect.width, character_rect.height // 4)
        if not check_collision(lower_mask_rect, obstacle_rect):
            character_rect = new_rect
            break
    # Check collision with masks
    for mask in mask_array:
        if check_collision_masks(character_mask, mask):
            character_rect = new_rect

    return character_rect

def handle_events(character_rect, character_mask, lower_quarter_height, movement_value, obstacles_Array, masks_array):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect = move_character(character_rect, character_mask, 'left', movement_value, obstacles_Array, masks_array)
    if keys[pygame.K_RIGHT]:
        character_rect = move_character(character_rect, character_mask, 'right', movement_value, obstacles_Array, masks_array)
    if keys[pygame.K_UP]:
        character_rect = move_character(character_rect, character_mask, 'up', movement_value, obstacles_Array, masks_array)
    if keys[pygame.K_DOWN]:
        character_rect = move_character(character_rect, character_mask, 'down', movement_value, obstacles_Array, masks_array)

    lower_mask_rect = pygame.Rect(character_rect.left, character_rect.bottom - lower_quarter_height, character_rect.width, lower_quarter_height)
    return character_rect, lower_mask_rect

def move_character(character_rect, character_mask, direction, movement_value, obstacles, mask_array):
    new_rect = character_rect.copy()

    if direction == 'left':
        new_rect.x -= movement_value
    elif direction == 'right':
        new_rect.x += movement_value
    elif direction == 'up':
        new_rect.y -= movement_value
    elif direction == 'down':
        new_rect.y += movement_value

    for obstacle_rect in obstacles:
        lower_mask_rect = pygame.Rect(new_rect.left, new_rect.bottom - character_rect.height // 4, character_rect.width, character_rect.height // 4)
        if not lower_mask_rect.colliderect(obstacle_rect):
            character_rect = new_rect
            break

    for mask in mask_array:
        if character_mask.overlap(mask, ( mask.get_rect().x - lower_mask_rect.x, mask.get_rect().y - lower_mask_rect.y )):
            character_rect = new_rect

    return character_rect
