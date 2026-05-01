import pygame


def get_shape_points(mode, x1, y1, x2, y2):
    # This function calculates points for each shape.
    # x1, y1 are the start mouse position.
    # x2, y2 are the current or final mouse position.

    if mode == 'square':
        # For a square, width and height must be equal.
        # We take the smaller distance between x and y.
        size = min(abs(x2 - x1), abs(y2 - y1))

        # If the mouse moves to the left, square starts from x1 - size.
        if x2 < x1:
            left = x1 - size
        else:
            left = x1

        # If the mouse moves up, square starts from y1 - size.
        if y2 < y1:
            top = y1 - size
        else:
            top = y1

        # Return rectangle for drawing square.
        return pygame.Rect(left, top, size, size)

    elif mode == 'right_triangle':
        # Right triangle has three points.
        # One point is the start position.
        # Other two points are based on mouse position.
        return [(x1, y1), (x2, y1), (x1, y2)]

    elif mode == 'equilateral_triangle':
        # Equilateral triangle has all sides equal.
        # We calculate height using formula: h = sqrt(3) / 2 * side.
        length = abs(x2 - x1)
        height = (3 ** 0.5) / 2 * length

        # If mouse moves left, triangle goes to the left.
        if x2 < x1:
            length = -length

        # If mouse moves down, triangle goes down.
        if y2 > y1:
            height = -height

        # Three points of the triangle.
        coord1 = (x1, y1)
        coord2 = (x1 + length, y1)
        coord3 = (x1 + length / 2, y1 - height)

        return [coord1, coord2, coord3]

    elif mode == 'rhombus':
        # Rhombus is drawn using four points.
        # First we find the center of the rhombus.
        x_c = (x1 + x2) // 2
        y_c = (y1 + y2) // 2

        # Half width and half height of the rhombus.
        x_w = abs(x2 - x1) // 2
        y_l = abs(y2 - y1) // 2

        # Return four points: top, right, bottom, left.
        return [
            (x_c, y_c - y_l),
            (x_c + x_w, y_c),
            (x_c, y_c + y_l),
            (x_c - x_w, y_c)
        ]


def draw_shape(surface, mode, color, x1, y1, x2, y2):
    # This function draws the selected shape on the selected surface.
    # surface can be screen or canvas.

    if mode == 'square':
        # Get square rectangle and draw it.
        square = get_shape_points(mode, x1, y1, x2, y2)
        pygame.draw.rect(surface, color, square, 2)

    elif mode == 'right_triangle':
        # Get triangle points and draw polygon.
        points = get_shape_points(mode, x1, y1, x2, y2)
        pygame.draw.polygon(surface, color, points, 2)

    elif mode == 'equilateral_triangle':
        # Get equilateral triangle points and draw polygon.
        points = get_shape_points(mode, x1, y1, x2, y2)
        pygame.draw.polygon(surface, color, points, 2)

    elif mode == 'rhombus':
        # Get rhombus points and draw polygon.
        points = get_shape_points(mode, x1, y1, x2, y2)
        pygame.draw.polygon(surface, color, points, 2)


def main():
    # Start pygame.
    pygame.init()

    # Create bigger screen.
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Paint")

    # Clock controls FPS.
    clock = pygame.time.Clock()

    # Canvas stores all finished drawings.
    # If we draw only on screen, preview would erase old shapes.
    canvas = pygame.Surface((1000, 700))
    canvas.fill((0, 0, 0))

    # Font for mode and color text.
    font = pygame.font.SysFont("Arial", 24)

    # This variable checks if mouse was pressed before.
    release_mouse = False

    # Start mouse position.
    x = 0
    y = 0

    # Default shape mode.
    mode = 'square'

    # Default color is white.
    color = (255, 255, 255)

    run = True

    while run:
        # Get pressed keyboard keys.
        pressed = pygame.key.get_pressed()

        # Check all events.
        for event in pygame.event.get():
            # Close window.
            if event.type == pygame.QUIT:
                run = False

        # Select shape mode.
        if pressed[pygame.K_1]:
            mode = 'square'

        if pressed[pygame.K_2]:
            mode = 'right_triangle'

        if pressed[pygame.K_3]:
            mode = 'equilateral_triangle'

        if pressed[pygame.K_4]:
            mode = 'rhombus'

        # Select color.
        if pressed[pygame.K_r]:
            color = (255, 0, 0)

        if pressed[pygame.K_g]:
            color = (0, 255, 0)

        if pressed[pygame.K_b]:
            color = (0, 0, 255)

        # Get mouse button state.
        mouse_click = pygame.mouse.get_pressed()

        # Get mouse position.
        mouse_cords = pygame.mouse.get_pos()

        # When left mouse button is pressed for the first time,
        # save the start position.
        if mouse_click[0] and not release_mouse:
            x, y = mouse_cords

        # When left mouse button is released,
        # draw the final shape on canvas.
        if not mouse_click[0] and release_mouse:
            x1, y1 = x, y
            x2, y2 = mouse_cords

            draw_shape(canvas, mode, color, x1, y1, x2, y2)

        # Draw saved canvas on screen.
        screen.blit(canvas, (0, 0))

        # If mouse is pressed, draw shape preview on screen.
        # This preview follows the mouse.
        if mouse_click[0]:
            x1, y1 = x, y
            x2, y2 = mouse_cords

            draw_shape(screen, mode, color, x1, y1, x2, y2)

        # Draw top panel for information.
        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 1000, 40))

        # Create text with current mode and color.
        text = font.render(
            f"Mode: {mode}   Color: {color}   1-Square  2-Right Triangle  3-Equilateral Triangle  4-Rhombus   R/G/B-Colors",
            True,
            (255, 255, 255)
        )

        # Show text on the screen.
        screen.blit(text, (10, 8))

        # Save current mouse state for the next frame.
        release_mouse = mouse_click[0]

        # Update display.
        pygame.display.flip()

        # Limit game to 60 FPS.
        clock.tick(60)


# Run main function.
main()

# Close pygame.
pygame.quit()