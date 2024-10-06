import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player = pygame.Rect((300, 250, 50, 50))

background = pygame.image.load('/Users/williamhutchinson/python-game-project/assets/game-background1.png')


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('assets', 'knight.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


def gameBackground(background):
    size = pygame.transform.scale(background, (800, 600))
    screen.blit(size, (0, 0))


gameRun = True
while (gameRun):

    screen.fill((0, 0, 0))

    gameBackground(background)

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # gameBackground(background)
    
    pygame.display.update()

pygame.quit()