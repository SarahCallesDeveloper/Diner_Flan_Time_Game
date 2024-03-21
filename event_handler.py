import pygame
from initialize import Waitress, obstacles_Array, masks_array

def check_collision(lower_mask_rect, obstacle_rect):
    return lower_mask_rect.colliderect(obstacle_rect)

def check_collision_masks(mask_rect, mask):
    return Waitress.lower_mask.overlap(mask, (mask.get_rect().x - mask_rect.x, mask.get_rect().y - mask_rect.y))

def move_character(character, direction, movement_value):
    new_rect = character.rect.copy()

    if direction == 'left':
        new_rect.x -= movement_value
    elif direction == 'right':
        new_rect.x += movement_value
    elif direction == 'up':
        new_rect.y -= movement_value
    elif direction == 'down':
        new_rect.y += movement_value

    for obstacle_rect in obstacles_Array:
        lower_mask_rect = character.lower_mask_rect
        if not check_collision(lower_mask_rect, obstacle_rect):
            character.rect = new_rect
            

    for mask in masks_array:
        if check_collision_masks(character.rect, mask):
            character.rect = new_rect

    return character.rect

def handle_events(character, movement_value):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.rect = move_character(character, 'left', movement_value)
    if keys[pygame.K_RIGHT]:
        character.rect = move_character(character, 'right', movement_value)
    if keys[pygame.K_UP]:
        character.rect = move_character(character, 'up', movement_value)
    if keys[pygame.K_DOWN]:
        character.rect = move_character(character, 'down', movement_value)

    lower_mask_rect = pygame.Rect(character.rect.left, character.rect.bottom - character.lower_quarter_height, character.rect.width, character.lower_quarter_height)
    return character.rect, lower_mask_rect

