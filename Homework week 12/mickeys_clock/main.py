import pygame
from clock import draw_clock

pygame.init()

WIDTH, HEIGHT = 600,600

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Mickey Mouse")

hand_image = pygame.image.load("images/mickey_mouse.png")

hand_image = pygame.transform.scale(hand_image, (300,50))

center = (WIDTH//2, HEIGHT//2)

running = True

while running:
    window.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock(window, hand_image, center)

    pygame.display.flip()

pygame.quit()