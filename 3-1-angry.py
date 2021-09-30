import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

def fon_lichika(x,y):
    circle(screen, (255, 255, 0), (x, y), 100)
    circle(screen, (0, 0, 0), (x, y), 100 , 2)
def glaziki(x,y):
    circle(screen, (255, 0, 0), (x, y), 20 , 0)
    circle(screen, (0, 0, 0), (x, y), 20 , 2)
    circle(screen, (0, 0, 0), (x, y), 8 , 0)
def rotik(x,y):
    rect(screen, (0, 0, 0), (x, y, 100, 20 ) , 0)
def brov(a,b,c,d,k,l):
    polygon(screen, (0, 0, 0), [(a,b), (a-k,b+l),
                               (c,d), (c+k,d-l)], 0)

rect(screen, (217, 217, 217), (0, 0, 400, 400),0)

fon_lichika(200,200)

glaziki(150,175)
glaziki(250,175)

rotik(150,250)
brov(200-18,200-34-5,200-104,200-78-5,6,9)
brov(200+20-5,200-36-7,200+102-5,200-58-7,-5,8)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True