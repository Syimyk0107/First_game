import pygame

pygame.init()

display = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Hi! This is my first game!')
icon = pygame.image.load('images/Code.webp')
pygame.display.set_icon(icon)

run = True
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            pygame.quit()      
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                display.fill((50, 100, 180))
            elif event.key == pygame.K_b:
                display.fill((255,255,200))    
            elif event.key == pygame.K_c:
                display.fill((25,255,200))    
            elif event.key == pygame.K_d:
                display.fill((250,255,250))    
            elif event.key == pygame.K_e:
                display.fill((150,200,255))    
    

            
    

