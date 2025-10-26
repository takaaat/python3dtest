import pygame
import sys
import numpy as np
import math

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

angle_x = 0
angle_y = 0

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("描画")
    return screen

def handle_events():
    global angle_x, angle_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()
    delta = 0.2
    if keys[pygame.K_UP]:
        angle_x -= delta
    if keys[pygame.K_DOWN]:
        angle_x += delta
    if keys[pygame.K_LEFT]:
        angle_y += delta
    if keys[pygame.K_RIGHT]:
        angle_y -= delta

    return True

def draw_objects(screen):
    screen.fill(WHITE)
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"theta_x: {angle_x}, theta_y: {angle_y}", True, BLACK)
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(text, text_rect)
    points = [
        [100, 100, 100],
        [100, 100, -100],
        [100, -100, 100],
        [100, -100, -100],
        [-100, 100, 100],
        [-100, 100, -100],
        [-100, -100, 100],
        [-100, -100, -100],
    ]
    radian_x = math.radians(angle_x)
    radian_y = math.radians(angle_y)
    rotate_y = np.array([[math.cos(radian_y), 0, math.sin(radian_y)], [0, 1, 0], [-math.sin(radian_y), 0, math.cos(radian_y)]])
    rotate_x = np.array([[1, 0, 0], [0, math.cos(radian_x), -math.sin(radian_x)], [0, math.sin(radian_x), math.cos(radian_x)]])
    after_points = []
    for point in points:
        after_points.append(np.dot(rotate_x, np.dot(rotate_y, point)))
    fov = 400
    for point in after_points:
        screen_x = (point[0] * fov) / (point[2] + fov)
        screen_y = (point[1] * fov) / (point[2] + fov)
        draw_x = SCREEN_WIDTH / 2 + screen_x
        draw_y = SCREEN_HEIGHT / 2 + screen_y
        pygame.draw.circle(screen, BLUE, (draw_x, draw_y), 5)

def main():
    screen = init_pygame()
    
    running = True
    while running:
        running = handle_events()
        draw_objects(screen)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
