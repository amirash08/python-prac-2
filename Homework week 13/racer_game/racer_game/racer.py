import pygame
import sys
import random
import time
import os
from pygame.locals import *


# Start pygame
pygame.init()

# This is the folder where this Python file is located
# We use it to load images from the same folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# FPS means frames per second
# It controls how smooth the game is
FPS = 60
FramePerSec = pygame.time.Clock()


# Colors in RGB format
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)


# Screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900


# Road borders
# Cars and coins should stay between these two x positions
ROAD_LEFT = 170
ROAD_RIGHT = 440


# Game variables
SPEED = 5       # Speed of enemy car and coin
SCORE = 0       # Score for avoiding enemy cars
COINS = 0       # Number of collected coins


# Fonts for text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)


# Game Over text
game_over = font.render("Game Over", True, BLACK)


# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game with Coins")


# Load background image
background = pygame.image.load(os.path.join(BASE_DIR, "AnimatedStreet.png"))

# Resize background image to screen size
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))



class Enemy(pygame.sprite.Sprite):
    """
    This class creates the enemy car.
    The enemy car starts above the screen and moves down.
    """

    def __init__(self):
        # Start the Sprite class
        super().__init__()

        # Load enemy car image
        self.image = pygame.image.load(os.path.join(BASE_DIR, "Enemy.png")).convert_alpha()

        # Resize enemy car image
        self.image = pygame.transform.scale(self.image, (70, 130))

        # Get rectangle of the image
        # We use rect to control the position
        self.rect = self.image.get_rect()

        # Put enemy car above the screen
        # x position is random, but only on the road
        self.rect.center = (random.randint(ROAD_LEFT + 50, ROAD_RIGHT - 50), -130)

        # Create mask for better collision
        # Mask checks the real shape, not only the rectangle
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        Move the enemy car down.
        If it leaves the screen, put it back at the top.
        """

        global SCORE

        # Move enemy down
        self.rect.move_ip(0, SPEED)

        # If enemy car goes below the screen
        if self.rect.top > SCREEN_HEIGHT:
            # Add score because player avoided the enemy
            SCORE += 1

            # Put enemy car back above the screen
            self.rect.center = (random.randint(ROAD_LEFT + 50, ROAD_RIGHT - 50), -130)



class Player(pygame.sprite.Sprite):
    """
    This class creates the player car.
    The player can move left and right.
    """

    def __init__(self):
        super().__init__()

        # Load player car image
        self.image = pygame.image.load(os.path.join(BASE_DIR, "Player.png")).convert_alpha()

        # Resize player car image
        self.image = pygame.transform.scale(self.image, (70, 130))

        # Get rectangle of the image
        self.rect = self.image.get_rect()

        # Put player car at the bottom center of the road
        self.rect.center = ((ROAD_LEFT + ROAD_RIGHT) // 2, SCREEN_HEIGHT - 100)

        # Create mask for better collision
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        Move the player car.
        Left arrow moves the car left.
        Right arrow moves the car right.
        """

        # Get pressed keys
        pressed_keys = pygame.key.get_pressed()

        # Move left, but do not leave the road
        if self.rect.left > ROAD_LEFT:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Move right, but do not leave the road
        if self.rect.right < ROAD_RIGHT:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)



class Coin(pygame.sprite.Sprite):
    """
    This class creates the coin.
    The coin appears on the road and moves down.
    """

    def __init__(self):
        super().__init__()

        # Create transparent surface for the coin
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)

        # Draw yellow circle
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)

        # Draw black border around the coin
        pygame.draw.circle(self.image, BLACK, (15, 15), 15, 2)

        # Get rectangle of the coin
        self.rect = self.image.get_rect()

        # Put coin at random place
        self.respawn()

    def respawn(self):
        """
        Put the coin in a new random place.
        The coin appears above the screen, only on the road.
        """

        self.rect.center = (
            random.randint(ROAD_LEFT + 20, ROAD_RIGHT - 20),
            random.randint(-600, -50)
        )

    def move(self):
        """
        Move the coin down.
        If it leaves the screen, create it again at the top.
        """

        # Move coin down
        self.rect.move_ip(0, SPEED)

        # If coin goes below the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()



# Create player, enemy and coin objects
P1 = Player()
E1 = Enemy()
C1 = Coin()


# Group for enemy cars
enemies = pygame.sprite.Group()
enemies.add(E1)


# Group for coins
coins = pygame.sprite.Group()
coins.add(C1)


# Group for all sprites
# It helps to draw and move all objects
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


# Create event for increasing speed
INC_SPEED = pygame.USEREVENT + 1

# This event happens every 1000 milliseconds, so every 1 second
pygame.time.set_timer(INC_SPEED, 1000)



# Main game loop
while True:

    # Check all events
    for event in pygame.event.get():

        # If speed event happens, increase speed
        if event.type == INC_SPEED:
            SPEED += 0.5

        # If player closes the window, exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Draw background first
    DISPLAYSURF.blit(background, (0, 0))


    # Show score in the top left corner
    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))


    # Show coins in the top right corner
    coins_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))


    # Move player car
    P1.move()


    # Draw and move all sprites
    for entity in all_sprites:

        # Draw sprite on the screen
        DISPLAYSURF.blit(entity.image, entity.rect)

        # Player moves with keyboard, so we skip it here
        if entity != P1:
            entity.move()


    # Check collision between player and coin
    collected_coin = pygame.sprite.spritecollideany(P1, coins)

    # If player collects coin
    if collected_coin:
        # Increase coin counter
        COINS += 1

        # Move coin to a new place
        collected_coin.respawn()


    # Check collision between player and enemy
    # collide_mask gives more accurate collision
    if pygame.sprite.spritecollideany(P1, enemies, pygame.sprite.collide_mask):

        # Try to play crash sound
        # If crash.wav does not exist, ignore the error
        try:
            pygame.mixer.Sound("crash.wav").play()
        except:
            pass

        # Small pause after crash
        time.sleep(0.5)

        # Fill screen with red color
        DISPLAYSURF.fill(RED)

        # Show Game Over text
        DISPLAYSURF.blit(game_over, (30, 250))

        # Update screen
        pygame.display.update()

        # Remove all sprites
        for entity in all_sprites:
            entity.kill()

        # Wait 2 seconds
        time.sleep(2)

        # Close the game
        pygame.quit()
        sys.exit()


    # Update the screen
    pygame.display.update()

    # Limit FPS
    FramePerSec.tick(FPS)