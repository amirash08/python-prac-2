import pygame
from collections import deque


def get_square_rect(x1, y1, x2, y2):
    size = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        left = x1 - size
    else:
        left = x1

    if y2 < y1:
        top = y1 - size
    else:
        top = y1

    return pygame.Rect(left, top, size, size)


def get_rhombus_points(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    half_width = abs(x2 - x1) // 2
    half_height = abs(y2 - y1) // 2

    return [
        (center_x, center_y - half_height),
        (center_x + half_width, center_y),
        (center_x, center_y + half_height),
        (center_x - half_width, center_y)
    ]


def get_right_triangle_points(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x1, y2)]


def get_equilateral_triangle_points(x1, y1, x2, y2):
    length = abs(x2 - x1)
    height = (3 ** 0.5) / 2 * length

    if x2 < x1:
        length = -length

    if y2 > y1:
        height = -height

    p1 = (x1, y1)
    p2 = (x1 + length, y1)
    p3 = (x1 + length / 2, y1 - height)

    return [p1, p2, p3]


def draw_shape(surface, mode, color, size, x1, y1, x2, y2):
    if mode == "line":
        pygame.draw.line(surface, color, (x1, y1), (x2, y2), size)

    elif mode == "rect":
        rect = pygame.Rect(
            min(x1, x2),
            min(y1, y2),
            abs(x2 - x1),
            abs(y2 - y1)
        )
        pygame.draw.rect(surface, color, rect, size)

    elif mode == "square":
        rect = get_square_rect(x1, y1, x2, y2)
        pygame.draw.rect(surface, color, rect, size)

    elif mode == "circle":
        rect = pygame.Rect(
            min(x1, x2),
            min(y1, y2),
            abs(x2 - x1),
            abs(y2 - y1)
        )
        pygame.draw.ellipse(surface, color, rect, size)

    elif mode == "right_triangle":
        points = get_right_triangle_points(x1, y1, x2, y2)
        pygame.draw.polygon(surface, color, points, size)

    elif mode == "equilateral_triangle":
        points = get_equilateral_triangle_points(x1, y1, x2, y2)
        pygame.draw.polygon(surface, color, points, size)

    elif mode == "rhombus":
        points = get_rhombus_points(x1, y1, x2, y2)
        pygame.draw.polygon(surface, color, points, size)


def flood_fill(surface, start_x, start_y, fill_color, width, height, toolbar_height):
    if start_y < toolbar_height:
        return

    old_color = surface.get_at((start_x, start_y))
    new_color = pygame.Color(fill_color)

    if old_color == new_color:
        return

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if x < 0 or x >= width or y < toolbar_height or y >= height:
            continue

        if surface.get_at((x, y)) == old_color:
            surface.set_at((x, y), new_color)

            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))