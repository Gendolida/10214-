import sys
import pygame

WIDTH, HEIGHT = 640, 480
FPS = 60

def print_menu(screen, font):
    # 게임 이름 출력
    # 메뉴 "TYPING GAME", "CALCULATOR GAME", "EXIT"
    # 현재 선택된 값 앞에 ">" 출력  현재: TYPING GAME
    # text_surf = font.render("TYPING GAME", True, (255, 255, 255))
    # screen.blit(text_surf, (100, 100))
    MENU = ["TIMING GAME", "TYPING GAME", "CALCULATOR GAME", "EXIT"]

    for i, item in enumerate(MENU):
        screen.blit(font.render(item, True, (255, 255, 255)), (100, 50 * i))

    #screen.blit(font.render("TIMING GAME", True, (255, 255, 255)), (100, 50))
   # screen.blit(font.render("TYPING GAME", True, (255, 255, 255)), (100, 100))
   # screen.blit(font.render("CALCULATOR GAME", True, (255, 255, 255)), (100, 150))
   # screen.blit(font.render("EXIT GAME", True, (255, 255, 255)), (100, 200))
def main() -> None:
  pygame.init()
  font = pygame.font.SysFont(None, 36)
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("NEW GAME")
  clock = pygame.time.Clock()

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          print("key up")
        elif event.key == pygame.K_DOWN:
          print("key down")

    screen.fill((30, 32, 40))
    print_menu(screen, font)
    pygame.display.flip()
    clock.tick(FPS)

    pygame.quit()
    sys.exit()

  if __name__ == "__main__":
    main()