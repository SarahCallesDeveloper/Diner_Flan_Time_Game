import pygame
from initialize import *
from event_handler import handle_events
from rendering import render_screen

pygame.init()

clock = pygame.time.Clock()
movement_value = 5
running = True
while running:
    # Event Handling
    result = handle_events(Waitress, movement_value)
    if not result:
        running = False
    else:
        Waitress.rect, lower_mask_rect = result

    # Rendering
    render_screen(screen, floor_image, left_wall_image, middle_wall_image, right_wall_image, Waitress, mushroom_tables)

    clock.tick(60)

pygame.quit()
