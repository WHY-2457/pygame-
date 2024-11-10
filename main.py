import pygame
from sys import exit

def main():
    pygame.init()
    w, h = 192 * 4, 192 * 3
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('MyGame')
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(120)  # 一次循环最快 (1s/60fps)*1000 (ms)

if __name__ == "__main__":
    main()

