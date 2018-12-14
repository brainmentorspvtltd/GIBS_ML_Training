import random
import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

black = 0,0,0
white = 255,255,255
red = 255,0,0

class Ball():

    def __init__(self):
        self.x = random.randint(0, width - 50)
        self.y = random.randint(0, height - 50)
        self.moveX = 1
        self.moveY = 1

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -1
        elif self.x < 0:
            self.moveX = 1
        elif self.y > height - 50:
            self.moveY = -1
        elif self.y < 0:
            self.moveY = 1
        

##ball_1 = Ball()
##ball_2 = Ball()
##ball_3 = Ball()

n = 1000
balls = []
for i in range(n):
    ball = Ball()
    balls.append(ball)


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
##    pygame.draw.rect(screen, black, [ball_1.x,ball_1.y,50,50])
##    ball_1.update()
##
##    pygame.draw.rect(screen, black, [ball_2.x,ball_2.y,50,50])
##    ball_2.update()
##
##    pygame.draw.rect(screen, black, [ball_3.x,ball_3.y,50,50])
##    ball_3.update()

    for i in range(len(balls)):
        pygame.draw.rect(screen, black, [balls[i].x,
                                         balls[i].y,50,50])
        balls[i].update()

    pygame.display.flip()










