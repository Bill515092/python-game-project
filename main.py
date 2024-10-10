import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, x_vel, y_vel):
        super().__init__()
        self.rect = pygame.Rect(x, y, 20, 20) 
        self.position = (x, y)
        self.velocity = (x_vel, y_vel)
       
    
    def update(self):
        # self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0 ,0), self.rect.center, 10)
    
    def move_left(self, velocity=-1):
        self.velocity = (velocity, self.velocity[1])

    def move_right(self, velocity=1):
        self.velocity = (velocity, self.velocity[1])
    
    def move_up(self, velocity=-1):
        self.velocity = (self.velocity[0], velocity)

    def move_down(self, velocity=1):
        self.velocity = (self.velocity[0], velocity)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('/Users/williamhutchinson/python-game-project/assets/game-background1.png')

player = Player(320, 240, 0 ,0)
platform = pygame.Rect(50, 400, 100, 50)


def game_background(background):
    size = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(size, (0, 0))


game_run = True
while (game_run):

    screen.fill((0, 0, 0))
    #game_background(background)
    colour = WHITE
    
    if player.rect.colliderect(platform): 
        colour = RED
    pygame.draw.rect(screen, colour, platform)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left()
            elif event.key == pygame.K_d:
                player.move_right()
            elif event.key == pygame.K_w:
                player.move_up()
            elif event.key == pygame.K_s:
                player.move_down()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move_left(0) 
            elif event.key == pygame.K_d:
                player.move_right(0)
            elif event.key == pygame.K_w:
                player.move_up(0)
            elif event.key == pygame.K_s:
                player.move_down(0)


    player.update()

    player.draw(screen)
    
    pygame.display.update()

pygame.quit()