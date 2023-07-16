import sys
import pygame

pygame.init()

# initate game window
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400


clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game project")
Night_surface = pygame.image.load('background/Night.png').convert()
test_font= pygame.font.Font('font/Pixeltype.ttf', 40)
test_font= test_font.render('Game project',False, 'Dark red')


run = True
while run:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit
            sys.exit()            
    pygame.display.update()
    screen.blit(Night_surface,(0,0))
    screen.blit(test_font,(300,50))




