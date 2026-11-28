import sys
import pygame
import random

WIDTH, HEIGHT = 640, 480
FPS = 60

# 1. wait !
# 2. press space!
# 3. 시간을 재서 알려주는
def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 50)
    pygame.display.set_caption("Blank Window")
    clock = pygame.time.Clock()

    running = True
    mode = "wait"
    result = "game over"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if mode == "press":
                    result = "60sec"
                else:
                    result = "game over"
                mode ="result"
            elif event.key == pygame.K_r:
                mode ="wait"
            elif event.key == pygame.K_e:
                mode ="exit"
                running = False

        screen.fill((30, 32, 40))

        if mode =="wait" and random.randint(0, 100) == 0:
            mode = "press"

        if mode == "press":
            screen.blit(font.render("PRESS BUTTON!", True, (255, 255, 255)), (260, 200))
        elif mode == "wait":
            screen.blit(font.render("WAIT!", True, (255, 255, 255)), (260, 200))
        elif mode == "exit":
            screen.blit(font.render("BYE BYE!", True, (255, 255, 255)), (260, 200))
        else:
            screen.blit(font.render(result, True, (255, 255, 255)), (260, 200))
            screen.blit(font.render("PRESS R TO RESTART", True, (255, 255, 255)), (120, 240))
            screen.blit(font.render("PRESS E TO ESCAPE", True, (255, 255, 255)), (120, 280))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
  main()