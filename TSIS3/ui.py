import pygame
import sys


# Screen settings
WIDTH = 600
HEIGHT = 800

# Create one screen for the whole game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
DARK_GRAY = (40, 40, 40)
YELLOW = (255, 215, 0)
RED = (220, 0, 0)


# Fonts
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 55)


def draw_text(text, x, y, color=WHITE, used_font=font):
    # Draw text on the screen
    image = used_font.render(text, True, color)
    screen.blit(image, (x, y))


def draw_button(text, rect, mouse_pos):
    # Draw a simple button

    color = GRAY

    # Change button color when mouse is on it
    if rect.collidepoint(mouse_pos):
        color = DARK_GRAY

    # Draw button rectangle
    pygame.draw.rect(screen, color, rect)

    # Draw button border
    pygame.draw.rect(screen, WHITE, rect, 2)

    # Draw button text in center
    text_image = font.render(text, True, WHITE)
    text_rect = text_image.get_rect(center=rect.center)
    screen.blit(text_image, text_rect)


def username_screen():
    # Screen where player enters name

    name = ""

    while True:
        screen.fill(BLACK)

        draw_text("Enter your name:", 170, 250)
        draw_text(name, 250, 310, YELLOW)
        draw_text("Press ENTER to start", 170, 380)

        pygame.display.update()

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Keyboard typing
            if event.type == pygame.KEYDOWN:

                # Start game
                if event.key == pygame.K_RETURN:
                    if name == "":
                        return "Player"
                    return name

                # Delete last character
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                # Add character to name
                else:
                    if len(name) < 12:
                        name += event.unicode


def main_menu():
    # Main menu screen

    # Import here to avoid circular import problem
    from racer import game_loop

    while True:
        mouse_pos = pygame.mouse.get_pos()

        play_button = pygame.Rect(200, 300, 200, 60)
        quit_button = pygame.Rect(200, 390, 200, 60)

        screen.fill(BLACK)

        draw_text("RACER GAME", 140, 150, YELLOW, big_font)

        draw_button("Play", play_button, mouse_pos)
        draw_button("Quit", quit_button, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Start game
                if play_button.collidepoint(mouse_pos):
                    player_name = username_screen()
                    game_loop(player_name)

                # Quit game
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


def game_over_screen(name, score, distance, coins):
    # Game over screen

    from racer import game_loop

    while True:
        mouse_pos = pygame.mouse.get_pos()

        retry_button = pygame.Rect(200, 500, 200, 50)
        menu_button = pygame.Rect(200, 570, 200, 50)

        screen.fill(BLACK)

        draw_text("GAME OVER", 140, 120, RED, big_font)
        draw_text(f"Name: {name}", 220, 230)
        draw_text(f"Score: {score}", 220, 280)
        draw_text(f"Distance: {distance}", 220, 330)
        draw_text(f"Coins: {coins}", 220, 380)

        draw_button("Retry", retry_button, mouse_pos)
        draw_button("Main Menu", menu_button, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Restart game with same name
                if retry_button.collidepoint(mouse_pos):
                    game_loop(name)

                # Go back to main menu
                elif menu_button.collidepoint(mouse_pos):
                    return


def win_screen(name, score, distance, coins):
    # Win screen

    from racer import game_loop

    while True:
        mouse_pos = pygame.mouse.get_pos()

        retry_button = pygame.Rect(200, 500, 200, 50)
        menu_button = pygame.Rect(200, 570, 200, 50)

        screen.fill(BLACK)

        draw_text("YOU WIN!", 170, 120, YELLOW, big_font)
        draw_text(f"Name: {name}", 220, 230)
        draw_text(f"Score: {score}", 220, 280)
        draw_text(f"Distance: {distance}", 220, 330)
        draw_text(f"Coins: {coins}", 220, 380)

        draw_button("Retry", retry_button, mouse_pos)
        draw_button("Main Menu", menu_button, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Restart game
                if retry_button.collidepoint(mouse_pos):
                    game_loop(name)

                # Go back to main menu
                elif menu_button.collidepoint(mouse_pos):
                    return