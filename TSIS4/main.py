import pygame

# First initialize pygame
pygame.init()

# Import snake only after pygame is initialized
from snake import main_menu

# Start menu
main_menu()

# Close pygame
pygame.quit()
