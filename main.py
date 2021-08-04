import pygame, sys
from snake import *

WIDTH = 520
HEIGHT = 700
BORDER = 5
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

pygame.init()
clock = pygame.time.Clock()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption('Snake')
font = pygame.font.SysFont('comicsans', 50, True)
Snake = snake(5)
Apple = apple()

def redrawGameWindow():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, (0, HEIGHT - WIDTH, WIDTH, WIDTH),  BORDER)
    text = font.render("Score: " + str(Snake.appleEaten), 1, (0,0,255))
    WIN.blit(text, (20,40))
    Snake.drawSnake(WIN)
    if Apple.alive:
        Apple.drawApple(WIN)
    pygame.display.update()
    
    
    
        

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and Snake.tileArray[0].direction != 2:
            Snake.changeSnakeDirection(0)
        elif keys[pygame.K_UP] and Snake.tileArray[0].direction != 3:
            Snake.changeSnakeDirection(1)
        elif keys[pygame.K_RIGHT] and Snake.tileArray[0].direction != 0:
            Snake.changeSnakeDirection(2)
        elif keys[pygame.K_DOWN] and Snake.tileArray[0].direction != 1:
            Snake.changeSnakeDirection(3)
            
        if not Apple.alive:     # Apple has been eaten
            Apple.createApple(Snake)  # Then create a new one
            
        
        Snake.eatApple(Apple)

            
        Snake.move()
        

        if Snake.checkCollision():
            pygame.time.wait(1000)
            Snake.restart()
        redrawGameWindow()        
        clock.tick(15)
                
    
    



if __name__ == '__main__':
    main()
