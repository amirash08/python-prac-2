import pygame
import random
import sys
import os

from ui import screen, draw_text, game_over_screen, win_screen


# Game settings
WIDTH = 600
HEIGHT = 800
FPS = 60

clock = pygame.time.Clock()


# Folder paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "assets", "images")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)
BLUE = (0, 0, 255)


# Road settings
ROAD_LEFT = 120
ROAD_RIGHT = 480

# Three road lanes
LANES = [180, 300, 420]


def load_image(filename, size):
    # Load image from assets/images folder
    path = os.path.join(IMAGE_DIR, filename)

    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, size)

    return image


# Load images
road_image = load_image("road.png", (WIDTH, HEIGHT))

player_image = load_image("player.png", (60, 110))
enemy_image = load_image("enemy.png", (60, 110))
coin_image = load_image("coin.png", (35, 35))


class Player:
    # Player car class

    def __init__(self):
        # Player image
        self.image = player_image

        # Player rectangle
        self.rect = self.image.get_rect()

        # Start position
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

        # Player speed
        self.speed = 7

        # Player lives
        self.lives = 1

    def draw(self):
        # Draw player car
        screen.blit(self.image, self.rect)

    def move(self):
        # Move player left and right
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > ROAD_LEFT:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < ROAD_RIGHT:
            self.rect.x += self.speed


class FallingObject:
    # Class for enemy cars, coins, oil and nitro

    def __init__(self, kind):
        self.kind = kind

        # Select image or size by object type
        if self.kind == "traffic":
            self.image = enemy_image
            self.rect = self.image.get_rect()

        elif self.kind == "coin":
            self.image = coin_image
            self.rect = self.image.get_rect()

        elif self.kind == "oil":
            # Oil is drawn manually, no image needed
            self.image = None
            self.rect = pygame.Rect(0, 0, 65, 40)

        elif self.kind == "nitro":
            # Nitro is drawn manually, no image needed
            self.image = None
            self.rect = pygame.Rect(0, 0, 40, 40)

        # Object speed
        self.speed = random.randint(4, 7)

        # Put object above screen
        self.reset()

    def reset(self):
        # Put object in random lane above screen
        lane = random.choice(LANES)

        self.rect.centerx = lane
        self.rect.y = random.randint(-1000, -100)

    def move(self, extra_speed):
        # Move object down
        self.rect.y += self.speed + extra_speed

        # If object leaves the screen, return it to top
        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self):
        # Draw object depending on its type

        if self.kind == "traffic":
            screen.blit(self.image, self.rect)

        elif self.kind == "coin":
            screen.blit(self.image, self.rect)

        elif self.kind == "oil":
            # Draw black oil puddle
            pygame.draw.ellipse(screen, BLACK, self.rect)
            pygame.draw.ellipse(screen, WHITE, self.rect, 2)

        elif self.kind == "nitro":
            # Draw blue nitro box
            pygame.draw.rect(screen, BLUE, self.rect)
            pygame.draw.rect(screen, WHITE, self.rect, 2)

            # Draw N letter on nitro
            draw_text("N", self.rect.x + 8, self.rect.y + 3, WHITE)


def game_loop(player_name):
    # Main game loop

    player = Player()

    # Game variables
    coins = 0
    score = 0
    distance = 0

    # Finish distance
    finish_distance = 3000

    # Base speed of the game
    base_speed = 3

    # Power-up variables
    active_power = None
    power_timer = 0

    # Create all falling objects
    objects = [
        FallingObject("traffic"),
        FallingObject("traffic"),

        FallingObject("oil"),
        FallingObject("oil"),

        FallingObject("coin"),
        FallingObject("coin"),
        FallingObject("coin"),

        FallingObject("nitro")
    ]

    running = True

    while running:
        clock.tick(FPS)

        # Check events
        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move player
        player.move()

        # Increase distance
        distance += 1

        # Score depends on distance and coins
        score = distance + coins * 10

        # Remaining distance to finish
        remaining = max(0, finish_distance - distance)

        # Game becomes faster every 500 distance points
        extra_speed = distance // 500

        # Power-up timer
        if active_power is not None:
            power_timer -= 1

            # If power time is over, remove power
            if power_timer <= 0:
                active_power = None

        # Nitro makes objects move faster
        nitro_speed = 0

        if active_power == "nitro":
            nitro_speed = 4

        # Move all objects
        for obj in objects:
            obj.move(base_speed + extra_speed + nitro_speed)

        # Check collisions
        for obj in objects:

            if player.rect.colliderect(obj.rect):

                # Coin gives points
                if obj.kind == "coin":
                    coins += 1
                    obj.reset()

                # Nitro power-up
                elif obj.kind == "nitro":
                    active_power = "nitro"
                    power_timer = FPS * 4
                    obj.reset()

                # Dangerous objects
                elif obj.kind in ["traffic", "oil"]:

                    # Lose one life
                    if player.lives > 0:
                        player.lives -= 1
                        obj.reset()

                    # No lives means game over
                    else:
                        game_over_screen(player_name, score, distance, coins)
                        return

        # If player reaches finish distance
        if distance >= finish_distance:
            win_screen(player_name, score + 500, distance, coins)
            return

        # Draw road
        screen.blit(road_image, (0, 0))

        # Draw all falling objects
        for obj in objects:
            obj.draw()

        # Draw player
        player.draw()

        # Draw game information
        draw_text(f"Name: {player_name}", 10, 10)
        draw_text(f"Score: {score}", 10, 45)
        draw_text(f"Coins: {coins}", 10, 80)
        draw_text(f"Distance: {distance}", 10, 115)
        draw_text(f"Remaining: {remaining}", 10, 150)
        draw_text(f"Lives: {player.lives}", 10, 185)

        # Draw active power information
        if active_power:
            seconds = power_timer // FPS
            draw_text(f"Power: {active_power} {seconds}s", 330, 10, YELLOW)
        else:
            draw_text("Power: none", 390, 10)

        # Update screen
        pygame.display.update()