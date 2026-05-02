import pygame

# Start pygame first
pygame.init()

# Import menu only after pygame is initialized
from ui import main_menu

# Start the program
main_menu()

# Close pygame
pygame.quit()