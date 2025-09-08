import pygame
import sys

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("描画")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def draw_objects(screen):
    screen.fill(WHITE)
    pygame.draw.line(screen, BLUE, (50, 50), (100, 200), 4)

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
