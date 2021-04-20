import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1070, 710))
fps = pygame.time.Clock()
black = (0, 0, 0)
running = True
c = 0

bg = pygame.image.load('background.png')
girl = pygame.image.load('girl.png')
girl = pygame.transform.scale(girl, (450, 700))
girl_talk = pygame.image.load('girl_talk.png')
girl_talk = pygame.transform.scale(girl_talk, (450, 700))
girl_blink1 = pygame.image.load('girl_blink1.png')
girl_blink1 = pygame.transform.scale(girl_blink1, (450, 700))
girl_blink2 = pygame.image.load('girl_blink2.png')
girl_blink2 = pygame.transform.scale(girl_blink2, (450, 700))

start = pygame.image.load('start.png')
start = pygame.transform.scale(start, (500, 200))

keys = pygame.key.get_pressed()
          
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(black)
    screen.blit(bg, (0, 0))
    
    if c == 0:
        screen.blit(girl, (500, 0))
        screen.blit(start, (0, 200))
    if keys[pygame.K_SPACE]:
        c += 1

    fps.tick(60)

    
    pygame.display.update()
    pygame.display.set_caption('game')
