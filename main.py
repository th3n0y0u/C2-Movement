import pygame

class Soop:
  def __init__(self):
    self.image = pygame.image.load("soop.png")
    self.speed = (0,1)
    self.rect = self.image.get_rect()

def main():
  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  soop = Soop()
  
  while True:
    screen.fill((0, 0, 0)) # RGB value
    screen.blit(soop.image, soop.rect)

  if __name__ == "__main__":
    main()