import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

black = 0,0,0
white = 255,255,255
red = 255,0,0

x = 0
y = 0

moveX = 1
moveY = 1

game = True

while game:

    # will return a list of events available in pygame
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill(white)
    # surface,color,[x,y,w,h]
    pygame.draw.rect(screen, black, [x,y,50,50])
    #pygame.draw.circle()
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.flip()










