import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1070, 710))
fps = pygame.time.Clock()
black = (0, 0, 0)
running = True
c = 0

bg = pygame.image.load('background.png')

ganyu = pygame.image.load('ganyu.png')


start = pygame.image.load('start.png')
start = pygame.transform.scale(start, (600, 200))

start2 = pygame.image.load('start2.png')
start2 = pygame.transform.scale(start2, (600, 200))

start3 = pygame.image.load('start3.png')
start3 = pygame.transform.scale(start3, (600, 200))

start4 = pygame.image.load('start4.png')
start4 = pygame.transform.scale(start4, (600, 200))

cow = pygame.image.load('cow.png')
cow = pygame.transform.scale(cow, (100, 100))

chicken1 = pygame.image.load('chicken1.png')
chicken1 = pygame.transform.scale(chicken1, (100, 100))

chicken2 = pygame.image.load('chicken2.png')
chicken2 = pygame.transform.scale(chicken2, (100, 100))

a = 0
b = 0
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(black)
    screen.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()

    if c == 0:
        screen.blit(start, (200, 200))
    if c == 0 and keys[pygame.K_SPACE]:
        screen.blit(bg, (0, 0))
        screen.blit(start, (200, 200))
        screen.blit(bg, (0, 0))
        screen.blit(start2, (200, 200))
        screen.blit(start2, (200, 200))
        screen.blit(start2, (200, 200))
        screen.blit(start2, (200, 200))
        screen.blit(start2, (200, 200))
        screen.blit(bg, (0, 0))
        screen.blit(start3, (200, 200))
        screen.blit(start3, (200, 200))
        screen.blit(start3, (200, 200))
        screen.blit(start3, (200, 200))
        screen.blit(start3, (200, 200))
        screen.blit(bg, (0, 0))
        screen.blit(start4, (200, 200))
        screen.blit(start4, (200, 200))
        screen.blit(start4, (200, 200))
        screen.blit(start4, (200, 200))
        screen.blit(start4, (200, 200))
        c += 1
    
    if c >= 1:
        screen.blit(ganyu, (-180, 0))

    fps.tick(60)
    
    pygame.display.update()
    pygame.display.set_caption('game')
