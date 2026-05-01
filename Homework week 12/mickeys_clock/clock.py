import pygame
from datetime import datetime


def draw_clock(window, hand_image, center):
    now_time= datetime.now()

    minutes = now_time.minute

    seconds = now_time.second

    min_angle = -(minutes * 6)

    sec_angle = -(seconds * 6)

    min_hand = pygame.transform.rotate(hand_image, min_angle)

    sec_hand = pygame.transform.rotate(hand_image, sec_angle)

    min_square = min_hand.get_rect(center = center)

    sec_square = sec_hand.get_rect(center = center)

    window.blit(min_hand, min_square)

    window.blit(sec_hand, sec_square)


                                      


