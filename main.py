import pygame
import random
import math
pygame.init()
pygame.display.set_caption("Random Circles")
screen = pygame.display.set_mode((800,800))

def hypotenuse(a, b):
    return  math.sqrt(a ** 2 ) + (b ** 2)
sum = hypotenuse(6,5)
print(sum)

def circle(z):
    for i in range (z):
     pygame.draw.circle(screen, (255, 255, 255), (random.randrange(0,800), random.randrange(0,800)), 20)

circle(20)
pygame.display.flip()

def shapes(c):
    if c == 'r':
        pygame.draw.rect(screen, (100, 0, 100), (random.randrange(0,800), random.randrange(0,800), 50, 50))
    elif c == 'c':
        pygame.draw.circle(screen, (100, 0, 100), (random.randrange(0,800), random.randrange(0,800)), 50)
    elif c == 't':
        pygame.draw.polygon(screen, (100, 0, 100), ((random.randrange(0,800), random.randrange(0,800)), (random.randrange(0,800), random.randrange(0,800)), (random.randrange(0,800), random.randrange(0,800))))

c= (input("r to draw rectangle, c to draw circle, t to draw triangle"))
shapes(c)
pygame.display.flip()
