import pygame
from datetime import datetime

# Import helper functions from tools.py
from tools import draw_shape, flood_fill


pygame.init()

# Window size
WIDTH = 1000
HEIGHT = 700

# Top toolbar height
TOOLBAR_HEIGHT = 50

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
GRAY = (40, 40, 40)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Clock controls FPS
clock = pygame.time.Clock()

# Canvas is where final drawings are saved
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Fonts
font = pygame.font.SysFont("Arial", 22)
text_font = pygame.font.SysFont("Arial", 28)

# Current tool
mode = "pencil"

# Current color
color = BLACK

# Current brush size
brush_size = 5

# Mouse variables
drawing = False
start_pos = None
last_pos = None

# Text tool variables
typing = False
text_position = None
typed_text = ""


def draw_toolbar():
    # Draw the top toolbar
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    # Information text
    info = (
        f"Tool: {mode} | Size: {brush_size} | "
        "P-Pencil L-Line R-Rect S-Square C-Circle "
        "Z-RightTri X-EqTri V-Rhombus F-Fill T-Text "
        "1/2/3 Size Q/W/E/A Colors Ctrl+S Save"
    )

    text = font.render(info, True, WHITE)
    screen.blit(text, (10, 12))


def save_canvas():
    # Create filename using current date and time
    now = datetime.now()
    filename = now.strftime("paint_%Y%m%d_%H%M%S.png")

    # Save canvas as PNG image
    pygame.image.save(canvas, filename)

    print("Saved:", filename)


running = True

while running:
    # Get current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check all events
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Keyboard events
        if event.type == pygame.KEYDOWN:

            # Save picture with Ctrl + S
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

            # If text tool is active
            elif typing:

                # Enter confirms text
                if event.key == pygame.K_RETURN:
                    text_surface = text_font.render(typed_text, True, color)
                    canvas.blit(text_surface, text_position)

                    typing = False
                    typed_text = ""
                    text_position = None

                # Escape cancels text
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    typed_text = ""
                    text_position = None

                # Backspace deletes last letter
                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]

                # Add typed character
                else:
                    typed_text += event.unicode

            else:
                # Select tools
                if event.key == pygame.K_p:
                    mode = "pencil"

                elif event.key == pygame.K_l:
                    mode = "line"

                elif event.key == pygame.K_r:
                    mode = "rect"

                elif event.key == pygame.K_s:
                    mode = "square"

                elif event.key == pygame.K_c:
                    mode = "circle"

                elif event.key == pygame.K_z:
                    mode = "right_triangle"

                elif event.key == pygame.K_x:
                    mode = "equilateral_triangle"

                elif event.key == pygame.K_v:
                    mode = "rhombus"

                elif event.key == pygame.K_f:
                    mode = "fill"

                elif event.key == pygame.K_t:
                    mode = "text"

                # Select brush size
                elif event.key == pygame.K_1:
                    brush_size = 2

                elif event.key == pygame.K_2:
                    brush_size = 5

                elif event.key == pygame.K_3:
                    brush_size = 10

                # Select colors
                elif event.key == pygame.K_q:
                    color = BLACK

                elif event.key == pygame.K_w:
                    color = RED

                elif event.key == pygame.K_e:
                    color = BLUE

                elif event.key == pygame.K_a:
                    color = GREEN

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Left mouse button
            if event.button == 1:
                x, y = event.pos

                # Do not draw on toolbar
                if y < TOOLBAR_HEIGHT:
                    continue

                # Fill tool
                if mode == "fill":
                    flood_fill(canvas, x, y, color, WIDTH, HEIGHT, TOOLBAR_HEIGHT)

                # Text tool
                elif mode == "text":
                    typing = True
                    text_position = (x, y)
                    typed_text = ""

                # Other drawing tools
                else:
                    drawing = True
                    start_pos = (x, y)
                    last_pos = (x, y)

        # Mouse button released
        if event.type == pygame.MOUSEBUTTONUP:

            # Left mouse button
            if event.button == 1 and drawing:
                x1, y1 = start_pos
                x2, y2 = event.pos

                # Pencil already draws while mouse moves
                if mode != "pencil":
                    draw_shape(canvas, mode, color, brush_size, x1, y1, x2, y2)

                drawing = False
                start_pos = None
                last_pos = None

        # Mouse movement
        if event.type == pygame.MOUSEMOTION:

            # Pencil draws continuously while mouse is moving
            if drawing and mode == "pencil":
                current_pos = event.pos

                pygame.draw.line(canvas, color, last_pos, current_pos, brush_size)

                last_pos = current_pos

    # Draw saved canvas
    screen.blit(canvas, (0, 0))

    # Preview for line and shapes
    if drawing and mode != "pencil":
        x1, y1 = start_pos
        x2, y2 = mouse_pos

        draw_shape(screen, mode, color, brush_size, x1, y1, x2, y2)

    # Preview for text
    if typing and text_position is not None:
        text_surface = text_font.render(typed_text, True, color)
        screen.blit(text_surface, text_position)

    # Draw toolbar on top
    draw_toolbar()

    # Update screen
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)


pygame.quit()