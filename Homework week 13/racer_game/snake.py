import pygame
import random
import sys


# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Size of one snake block
BLOCK_SIZE = 20

# Wall thickness
WALL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
GRAY = (80, 80, 80)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock controls game speed
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 60)


def draw_text(text, color, x, y, font_type=font):
    # Draw text on the screen
    label = font_type.render(text, True, color)
    screen.blit(label, (x, y))


def draw_walls():
    # Draw visible wall border around playing area
    pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, WALL_SIZE))
    pygame.draw.rect(screen, GRAY, (0, SCREEN_HEIGHT - WALL_SIZE, SCREEN_WIDTH, WALL_SIZE))
    pygame.draw.rect(screen, GRAY, (0, 0, WALL_SIZE, SCREEN_HEIGHT))
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - WALL_SIZE, 0, WALL_SIZE, SCREEN_HEIGHT))


def generate_food(snake):
    """
    Generate random food position.
    Food must not appear on the wall or on the snake.
    """
    while True:
        x = random.randrange(WALL_SIZE, SCREEN_WIDTH - WALL_SIZE, BLOCK_SIZE)
        y = random.randrange(WALL_SIZE, SCREEN_HEIGHT - WALL_SIZE, BLOCK_SIZE)

        food_position = [x, y]

        # Food cannot appear on snake body
        if food_position not in snake:
            return food_position


def draw_snake(snake):
    # Draw every block of the snake
    for block in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
        )


def draw_food(food):
    # Draw food as a red square
    pygame.draw.rect(
        screen,
        RED,
        pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
    )


def game_over_screen(score, level):
    # Show Game Over screen
    screen.fill(BLACK)

    draw_text("GAME OVER", RED, 140, 220, big_font)
    draw_text(f"Score: {score}", WHITE, 240, 300)
    draw_text(f"Level: {level}", WHITE, 240, 340)
    draw_text("Press ESC to exit", WHITE, 190, 390)

    pygame.display.update()

    # Wait until user presses ESC or closes the window
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def main():
    # Starting position of the snake
    snake = [
        [300, 300],
        [280, 300],
        [260, 300]
    ]

    # Starting direction
    direction = "RIGHT"
    change_to = direction

    # Generate first food
    food = generate_food(snake)

    # Score and level
    score = 0
    level = 1

    # Starting speed
    speed = 8

    run = True

    while run:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Change snake direction with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        # Prevent snake from moving directly backward
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        elif change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        elif change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        elif change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        # Current head position
        head_x = snake[0][0]
        head_y = snake[0][1]

        # Move head
        if direction == "UP":
            head_y -= BLOCK_SIZE
        elif direction == "DOWN":
            head_y += BLOCK_SIZE
        elif direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        # If snake goes through the wall, it appears from the opposite side
        if head_x < WALL_SIZE:
            head_x = SCREEN_WIDTH - WALL_SIZE - BLOCK_SIZE

        elif head_x >= SCREEN_WIDTH - WALL_SIZE:
            head_x = WALL_SIZE

        elif head_y < WALL_SIZE:
            head_y = SCREEN_HEIGHT - WALL_SIZE - BLOCK_SIZE

        elif head_y >= SCREEN_HEIGHT - WALL_SIZE:
            head_y = WALL_SIZE

        # New head position after wall wrap
        new_head = [head_x, head_y]

        # Check self collision
        if new_head in snake:
            game_over_screen(score, level)

        # Add new head to the snake
        snake.insert(0, new_head)

        # Check if snake eats food
        if new_head == food:
            score += 1

            # Generate new food not on snake and not on wall
            food = generate_food(snake)

            # Add new level every 4 foods
            if score % 4 == 0:
                level += 1
                speed += 2
        else:
            # If food was not eaten, remove tail
            snake.pop()

        # Draw everything
        screen.fill(BLACK)

        draw_walls()
        draw_snake(snake)
        draw_food(food)

        # Draw score, level and speed
        draw_text(f"Score: {score}", WHITE, 30, 30)
        draw_text(f"Level: {level}", WHITE, 30, 60)
        draw_text(f"Speed: {speed}", WHITE, 30, 90)

        pygame.display.update()

        # Control game speed
        clock.tick(speed)

    pygame.quit()
    sys.exit()


main()