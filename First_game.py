import pygame

pygame.init()

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hi! This is my first game!')
icon = pygame.image.load('images/Code.webp')
pygame.display.set_icon(icon)

font = pygame.font.Font(None, 100)
text = font.render("Game Over!!!", True, ('red'))  
text_rect = text.get_rect(center=(640 , 250))

background = pygame.image.load('background/gameing.jpg')
square = pygame.Surface((700, 400))
square.fill('black')

ghost = pygame.image.load('images/ghost/ghost.png')

player_left = [
    # pygame.image.load('images/left/left1.png'),
    # pygame.image.load('images/left/left2.png'),
    # pygame.image.load('images/left/left3.png'),
    # pygame.image.load('images/left/left4.png'),
    # pygame.image.load('images/left/left5.png'),
    # pygame.image.load('images/left/left6.png'),
    # pygame.image.load('images/left/left7.png'),
    # pygame.image.load('images/left/left8.png'),
    # pygame.image.load('images/left/left9.png'),
    # pygame.image.load('images/left/left10.png'),
    # pygame.image.load('images/left/left11.png'),
    # pygame.image.load('images/left/left12.png'),
    pygame.image.load('images/left/left13.png'),
    pygame.image.load('images/left/left14.png'),
    pygame.image.load('images/left/left15.png'),
    pygame.image.load('images/left/left16.png'),
    pygame.image.load('images/left/left17.png'),
    pygame.image.load('images/left/left18.png'),
    pygame.image.load('images/left/left19.png'),
    pygame.image.load('images/left/left20.png'),
]

player_right = [pygame.transform.flip(img, True, False) for img in player_left]

clock = pygame.time.Clock()

pygame.mixer.init()
music_playing = False
current_music = None
player_count = 0
back_x = 0

player_x = 900
player_y = 489
ghost_x = 1100
ghost_y = 289

jump = False
gr = 8

facing_right = False  

run = True
while run:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                if music_playing:
                    pygame.mixer.music.stop()  
                    music_playing = False

                if current_music == 'track1':
                    pygame.mixer.music.load('C:/Users/Notnik_kg/Music/Spring_Waltz.mp3')
                    pygame.mixer.music.play(-1, 0.0) 
                    current_music = 'track2'
                else:
                    pygame.mixer.music.load('C:/Users/Notnik_kg/Music/Mortal_Kombat.mp3')  
                    pygame.mixer.music.play(-1, 0.0)  
                    current_music = 'track1'
                music_playing = True


    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:  
        player_y -= 3  
    elif keys[pygame.K_DOWN]: 
        player_y += 3  
    elif keys[pygame.K_LEFT]:  
        player_x -= 3  
        facing_right = False 
    elif keys[pygame.K_RIGHT]: 
        player_x += 3  
        facing_right = True  


    back_x += 1
    if back_x >= 1280:
        back_x = 0

    display.blit(background, (back_x, 0)) 
    display.blit(background, (back_x - 1280, 0)) 

    ghost_x -= 1
    if ghost_x <= -1280:
        ghost_x = 0
    display.blit(ghost, (ghost_x, ghost_y+180)) 

    if not jump:
        if keys[pygame.K_SPACE]:  
            jump= True
    else:
        if gr>=-8:
            if gr>0:
                player_y -=(gr**2)/2
            else:
                player_y +=(gr**2)/2
            gr -=1
        else:
            jump = False
            gr = 8

    if facing_right:
        display.blit(player_right[player_count], (player_x, player_y))
    else:
        display.blit(player_left[player_count], (player_x, player_y))

    if player_count == 7:
        player_count = 0
    else:
        player_count += 1
    
    
               
    player_rect = player_right[0].get_rect(topleft=(player_x, player_y))
    ghost_rect = ghost.get_rect(topleft=(ghost_x, 489))
    if player_rect.colliderect(ghost_rect):
        print('Game Over !!!')
        square = pygame.Surface((700, 400))
        square.fill('black')
        break    
      
    pygame.draw.circle(display, 'white', (80, 40), 25)

    pygame.display.update() 

    clock.tick(100)  
   
pygame.quit()












