import pygame
import random

GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
SIZE = 15

class tile(object):
    def __init__(self, x, y, size = SIZE):
        self.size = size
        self.x = x
        self.y = y
        self.direction = 0
        self.contour = 2
        

class apple(object):
    def __init__(self):
        self.alive = False
        self.x = 0
        self.y = 0
    
    def createApple(self, Snake):      
        self.x, self.y = random.randint(0, 33)*15 + 5, random.randint(0, 33) * 15 + 185
        while ( Snake.checkIfContain(self.x, self.y)):
            self.x, self.y = random.randint(0, 33) * 15 + 5, random.randint(0, 33) * 15 + 185
        self.alive = True    
        
    def drawApple(self, win):
        pygame.draw.rect(win, RED, (self.x, self.y, SIZE, SIZE) )

        
        
        

class snake(object):
    def __init__(self, length):
        self.primaryLength = length
        self.length = length
        self.headx = 290
        self.heady = 485
        self.velocity = 15
        self.appleEaten = 0
        self.tileArray = []
        
        for i in range(self.length):
            self.tileArray.append(tile(self.headx + (i * SIZE), self.heady))
        
        
        
    def move(self):
        # iterating backwards
        for tile in self.tileArray[::-1]:
            if tile.direction == 0:
                tile.x -= self.velocity
            elif tile.direction == 1:
                tile.y -= self.velocity
            elif tile.direction == 2:
                tile.x += self.velocity
            else:
                tile.y += self.velocity
                
        for i in range(self.length - 1, 0, -1):
            self.tileArray[i].direction = self.tileArray[i-1].direction
                
                
    def drawSnake(self, win):
        for tile in self.tileArray:
            pygame.draw.rect(win, BLUE, (tile.x, tile.y, tile.size, tile.size) )
            pygame.draw.rect(win, GREEN, (tile.x+tile.contour, tile.y+tile.contour, tile.size - 2*tile.contour, tile.size- 2*tile.contour) )
            
            
    def changeSnakeDirection(self, direction):
        self.tileArray[0].direction = direction
        
    def checkCollision(self):
        # print('x', self.tileArray[0].x, 'y :', self.tileArray[0].y)
        
        if self.tileArray[0].x < 5 or self.tileArray[0].x + SIZE > 515:
            return True
        if self.tileArray[0].y < 185 or self.tileArray[0].y + SIZE >695:
            return True 
        for tile in self.tileArray[1:]:
            if self.tileArray[0].x == tile.x and self.tileArray[0].y == tile.y:
                return True
        return False
        
        
    def restart(self):
        self.headx = 290
        self.heady = 485
        self.length = self.primaryLength
        self.tileArray = []
        self.appleEaten = 0
        
        for i in range(self.primaryLength):
            self.tileArray.append(tile(self.headx + (i * SIZE), self.heady))
            
            
    # Checks if given coordinates are in snake's body, returns True if they are, False if not
    def checkIfContain(self, x, y):
        for tile in self.tileArray:
            if tile.x == x and tile.y == y:
                print('NO elooo')
                return True
        return False
    
    def eatApple(self, Apple):
        if self.tileArray[0].x == Apple.x and self.tileArray[0].y == Apple.y:
            Apple.alive = False
            self.length += 1
            if self.tileArray[-1].direction == 0:
                self.tileArray.append(tile(self.tileArray[-1].x+SIZE, self.tileArray[-1].y))
            if self.tileArray[-1].direction == 1:
                self.tileArray.append(tile(self.tileArray[-1].x, self.tileArray[-1].y+SIZE))
            if self.tileArray[-1].direction == 2:
                self.tileArray.append(tile(self.tileArray[-1].x-SIZE, self.tileArray[-1].y))
            if self.tileArray[-1].direction == 3:
                self.tileArray.append(tile(self.tileArray[-1].x, self.tileArray[-1].y-SIZE))

            self.tileArray[-1].direction = self.tileArray[-2].direction
            self.appleEaten += 1
    