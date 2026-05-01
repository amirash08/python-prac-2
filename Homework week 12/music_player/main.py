import pygame 
from player import *

pygame.init()

pygame.mixer.init()

window = pygame.display.set_mode((500, 300))

pygame.display.set_caption("Music player")

font_music = pygame.font.SysFont(None, 36)

run = True

while run:
    window.fill((255,255,255))

    music_name = font_music.render(f"Music: {track_info()}", (255,255,255), True)

    window.blit(music_name, (100, 85))

    menu = font_music.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (0,0,0))

    window.blit(menu, (50, 140))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()

            elif event.key == pygame.K_s:
                stop_music()

            elif event.key == pygame.K_n:
                next_music()
            
            elif event.key == pygame.K_b:
                prev_music()
            
            elif event.key == pygame.K_q:
                run = False

pygame.quit()
