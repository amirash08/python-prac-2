import pygame
import random
import sys

from database import save_game_result
from settings import load_settings, save_settings


# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLOCK_SIZE = 20
WALL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
RED = (220, 0, 0)
YELLOW = (255, 215, 0)
PURPLE = (160, 0, 200)
GRAY = (80, 80, 80)
ORANGE = (255, 140, 0)
CYAN = (0, 200, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 18)
big_font = pygame.font.SysFont("Arial", 60)


def draw_text(text, color, x, y, font_type=font):
    label = font_type.render(text, True, color)
    screen.blit(label, (x, y))


def get_snake_color(settings):
    if settings["snake_color"] == "blue":
        return BLUE
    elif settings["snake_color"] == "red":
        return RED
    else:
        return GREEN


def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, SCREEN_HEIGHT))

    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, (30, 30, 30), (0, y), (SCREEN_WIDTH, y))


def draw_walls():
    pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, WALL_SIZE))
    pygame.draw.rect(screen, GRAY, (0, SCREEN_HEIGHT - WALL_SIZE, SCREEN_WIDTH, WALL_SIZE))
    pygame.draw.rect(screen, GRAY, (0, 0, WALL_SIZE, SCREEN_HEIGHT))
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - WALL_SIZE, 0, WALL_SIZE, SCREEN_HEIGHT))


def draw_button(text, rect, mouse_pos):
    color = GRAY

    if rect.collidepoint(mouse_pos):
        color = (50, 50, 50)

    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, WHITE, rect, 2)

    text_image = font.render(text, True, WHITE)
    text_rect = text_image.get_rect(center=rect.center)

    screen.blit(text_image, text_rect)


def generate_position(snake):
    while True:
        x = random.randrange(WALL_SIZE, SCREEN_WIDTH - WALL_SIZE, BLOCK_SIZE)
        y = random.randrange(WALL_SIZE, SCREEN_HEIGHT - WALL_SIZE, BLOCK_SIZE)

        pos = [x, y]

        if pos not in snake:
            return pos


def generate_food(snake):
    position = generate_position(snake)

    weight = random.choice([1, 2, 3])
    spawn_time = pygame.time.get_ticks()
    life_time = 5000

    return position, weight, spawn_time, life_time


def generate_poison(snake):
    position = generate_position(snake)

    spawn_time = pygame.time.get_ticks()
    life_time = 7000

    return position, spawn_time, life_time


def generate_powerup(snake):
    position = generate_position(snake)

    power_type = random.choice(["slow", "double", "ghost"])
    spawn_time = pygame.time.get_ticks()
    life_time = 8000

    return position, power_type, spawn_time, life_time


def draw_snake(snake, color):
    for block in snake:
        pygame.draw.rect(
            screen,
            color,
            pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
        )


def draw_food(food, weight):
    if weight == 1:
        color = RED
    elif weight == 2:
        color = YELLOW
    else:
        color = PURPLE

    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
    )

    text = small_font.render(str(weight), True, BLACK)
    screen.blit(text, (food[0] + 5, food[1] + 1))


def draw_poison(poison):
    pygame.draw.rect(
        screen,
        ORANGE,
        pygame.Rect(poison[0], poison[1], BLOCK_SIZE, BLOCK_SIZE)
    )

    text = small_font.render("P", True, BLACK)
    screen.blit(text, (poison[0] + 5, poison[1] + 1))


def draw_powerup(powerup, power_type):
    pygame.draw.rect(
        screen,
        CYAN,
        pygame.Rect(powerup[0], powerup[1], BLOCK_SIZE, BLOCK_SIZE)
    )

    if power_type == "slow":
        letter = "S"
    elif power_type == "double":
        letter = "D"
    else:
        letter = "G"

    text = small_font.render(letter, True, BLACK)
    screen.blit(text, (powerup[0] + 5, powerup[1] + 1))


def username_screen():
    username = ""

    while True:
        screen.fill(BLACK)

        draw_text("Enter username:", WHITE, 160, 200)
        draw_text(username, YELLOW, 220, 270)
        draw_text("Press ENTER to play", WHITE, 150, 350)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username == "":
                        return "Player"
                    return username

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                else:
                    if len(username) < 12:
                        username += event.unicode


def settings_screen():
    settings = load_settings()

    while True:
        mouse_pos = pygame.mouse.get_pos()

        color_button = pygame.Rect(150, 200, 300, 60)
        grid_button = pygame.Rect(150, 290, 300, 60)
        sound_button = pygame.Rect(150, 380, 300, 60)
        back_button = pygame.Rect(200, 500, 200, 60)

        screen.fill(BLACK)

        draw_text("SETTINGS", YELLOW, 170, 100, big_font)

        draw_button(f"Color: {settings['snake_color']}", color_button, mouse_pos)
        draw_button(f"Grid: {settings['grid']}", grid_button, mouse_pos)
        draw_button(f"Sound: {settings['sound']}", sound_button, mouse_pos)
        draw_button("Back", back_button, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_settings(settings)
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if color_button.collidepoint(mouse_pos):
                    if settings["snake_color"] == "green":
                        settings["snake_color"] = "blue"
                    elif settings["snake_color"] == "blue":
                        settings["snake_color"] = "red"
                    else:
                        settings["snake_color"] = "green"

                elif grid_button.collidepoint(mouse_pos):
                    settings["grid"] = not settings["grid"]

                elif sound_button.collidepoint(mouse_pos):
                    settings["sound"] = not settings["sound"]

                elif back_button.collidepoint(mouse_pos):
                    save_settings(settings)
                    return


def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        play_button = pygame.Rect(200, 250, 200, 60)
        settings_button = pygame.Rect(200, 340, 200, 60)
        quit_button = pygame.Rect(200, 430, 200, 60)

        screen.fill(BLACK)

        draw_text("SNAKE GAME", YELLOW, 120, 100, big_font)

        draw_button("Play", play_button, mouse_pos)
        draw_button("Settings", settings_button, mouse_pos)
        draw_button("Quit", quit_button, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(mouse_pos):
                    username = username_screen()
                    game_loop(username)

                elif settings_button.collidepoint(mouse_pos):
                    settings_screen()

                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


def game_over_screen(username, score, level):
    save_game_result(username, score, level)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        retry_button = pygame.Rect(200, 420, 200, 60)
        menu_button = pygame.Rect(200, 500, 200, 60)

        screen.fill(BLACK)

        draw_text("GAME OVER", RED, 140, 150, big_font)
        draw_text(f"Player: {username}", WHITE, 190, 250)
        draw_text(f"Score: {score}", WHITE, 220, 300)
        draw_text(f"Level: {level}", WHITE, 220, 340)

        draw_button("Retry", retry_button, mouse_pos)
        draw_button("Menu", menu_button, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(mouse_pos):
                    game_loop(username)

                elif menu_button.collidepoint(mouse_pos):
                    return


def game_loop(username):
    settings = load_settings()

    snake_color = get_snake_color(settings)

    snake = [
        [300, 300],
        [280, 300],
        [260, 300]
    ]

    direction = "RIGHT"
    change_to = direction

    food, food_weight, food_spawn_time, food_life_time = generate_food(snake)
    poison, poison_spawn_time, poison_life_time = generate_poison(snake)
    powerup, power_type, power_spawn_time, power_life_time = generate_powerup(snake)

    score = 0
    level = 1
    speed = 8

    active_power = None
    active_power_end_time = 0

    running = True

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        elif change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        elif change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        elif change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        head_x = snake[0][0]
        head_y = snake[0][1]

        if direction == "UP":
            head_y -= BLOCK_SIZE
        elif direction == "DOWN":
            head_y += BLOCK_SIZE
        elif direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        # Snake appears from the opposite side
        if head_x < WALL_SIZE:
            head_x = SCREEN_WIDTH - WALL_SIZE - BLOCK_SIZE
        elif head_x >= SCREEN_WIDTH - WALL_SIZE:
            head_x = WALL_SIZE
        elif head_y < WALL_SIZE:
            head_y = SCREEN_HEIGHT - WALL_SIZE - BLOCK_SIZE
        elif head_y >= SCREEN_HEIGHT - WALL_SIZE:
            head_y = WALL_SIZE

        new_head = [head_x, head_y]

        # Ghost power ignores self collision
        if active_power != "ghost":
            if new_head in snake:
                game_over_screen(username, score, level)

        snake.insert(0, new_head)

        # Eat normal food
        if new_head == food:
            if active_power == "double":
                score += food_weight * 2
            else:
                score += food_weight

            food, food_weight, food_spawn_time, food_life_time = generate_food(snake)

            if score // 5 + 1 > level:
                level += 1
                speed += 2
        else:
            snake.pop()

        # Eat poison food
        if new_head == poison:
            if len(snake) <= 3:
                game_over_screen(username, score, level)
            else:
                snake.pop()
                snake.pop()

            poison, poison_spawn_time, poison_life_time = generate_poison(snake)

        # Eat power-up
        if new_head == powerup:
            active_power = power_type
            active_power_end_time = current_time + 5000

            powerup, power_type, power_spawn_time, power_life_time = generate_powerup(snake)

        # Food disappears after timer
        if current_time - food_spawn_time > food_life_time:
            food, food_weight, food_spawn_time, food_life_time = generate_food(snake)

        # Poison disappears after timer
        if current_time - poison_spawn_time > poison_life_time:
            poison, poison_spawn_time, poison_life_time = generate_poison(snake)

        # Power-up disappears after timer
        if current_time - power_spawn_time > power_life_time:
            powerup, power_type, power_spawn_time, power_life_time = generate_powerup(snake)

        # Remove active power after 5 seconds
        if active_power is not None and current_time > active_power_end_time:
            active_power = None

        screen.fill(BLACK)

        if settings["grid"]:
            draw_grid()

        draw_walls()
        draw_snake(snake, snake_color)
        draw_food(food, food_weight)
        draw_poison(poison)
        draw_powerup(powerup, power_type)

        food_time_left = max(0, (food_life_time - (current_time - food_spawn_time)) // 1000)

        draw_text(f"Player: {username}", WHITE, 30, 30)
        draw_text(f"Score: {score}", WHITE, 30, 60)
        draw_text(f"Level: {level}", WHITE, 30, 90)
        draw_text(f"Food time: {food_time_left}", WHITE, 30, 120)

        if active_power:
            power_left = max(0, (active_power_end_time - current_time) // 1000)
            draw_text(f"Power: {active_power} {power_left}s", YELLOW, 30, 150)
        else:
            draw_text("Power: none", WHITE, 30, 150)

        pygame.display.update()

        final_speed = speed

        if active_power == "slow":
            final_speed = max(4, speed - 4)

        clock.tick(final_speed)