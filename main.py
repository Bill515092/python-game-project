import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, x_vel, y_vel):
        super().__init__()
        self.position = (x, y)
        self.velocity = (x_vel, y_vel)
    
    def update(self):
        self.postion = (self.position[0], self.velocity[0], self.position[1])

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0 ,0), self.position, 10)
    
    def move_left(self):
        self.velocity = (-1, self.velocity[1])

    def move_right(self):
        self.velocity = (1, self.velocity[1])


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('/Users/williamhutchinson/python-game-project/assets/game-background1.png')

player = Player(320, 240, 0 ,0)


def gameBackground(background):
    size = pygame.transform.scale(background, (800, 600))
    screen.blit(size, (0, 0))


gameRun = True
while (gameRun):

    screen.fill((0, 0, 0))

    gameBackground(background)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left()
            elif event.key == pygame.K_d:
                player.move_right()
    
    player.update()

    player.draw(screen)
    
    pygame.display.update()

pygame.quit()