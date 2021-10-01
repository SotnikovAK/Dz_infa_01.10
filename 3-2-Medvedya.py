import pygame
import math
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 1000))

def fon(x,y):
    rect(screen, (0, 255, 255), (0, 0, 800, 500),0)
    rect(screen, (230, 230, 230), (0, 500, 800, 1000),0)
    line(screen, (0,0,0),(0,500),(800,500))

def nebo(x,y):
    r = int(240*k)
    A = 15
    circle(screen, (161, 249, 228), (x,y-A), r)
    circle(screen, (0, 255, 255), (x,y-A), int((240-50)*k))
    #first_perekladina
    polygon(screen, (161, 249, 228), [(x-r-5,y-int(25*k)-5-A), (x-r-5,y+int(15*k)-5-A),(x+r+5,y+int(25*k)+5-A), (x+r+5,y-int(15*k)+5-A)], 0)
    polygon(screen, (220, 247, 218), [(x-r,y-int(25*k)-5-A), (x-r,y+int(15*k)-5-A),(x-r+int(50*k),y+int(15*k)-5-A), (x-r+int(50*k),y-int(25*k)-3-A)], 0)
    polygon(screen, (220, 247, 218), [(x+r,y-int(15*k)+5-A), (x+r,y+int(25*k)+5-A),(x+r-int(50*k),y+int(25*k)+5-A), (x+r-int(50*k),y-int(15*k)+5-A)], 0)
    circle(screen, (255, 246, 213), (x-r+15,y-10-A), 15)
    circle(screen, (255, 246, 213), (x+r-17,y+10-A), 15)
    #second_perecladina
    polygon(screen, (161, 249, 228), [(x-40,y+r+5-A), (x-4,y+r+8-A),(x+40,y-r-10-A), (x-5,y-r-10-A)], 0)
    polygon(screen, (220, 247, 218), [(x-40,y+r-3-A), (x-4,y+r+1-A),(x+2,y+r-int(50*k)-A), (x-35,y+r-int(50*k)-5-A)], 0)
    circle(screen, (255, 246, 213), (x-20,y+r-20-A), 15)
    #circle_na_midu
    circle(screen, (255, 246, 213), (x,y-A), 25)

def luja(a,b,c,d):
    ellipse(screen,(77,77,77), (a,b,c,d),0)
    ellipse(screen,(0,0,0), (a,b,c,d),1)
    ellipse(screen,(22,80,68), (a+40,b+int(40*k),c-2*int(40*k),d-int(40*k)),0)
    ellipse(screen,(0,0,0), (a+40,b+int(40*k),c-2*int(40*k),d-int(40*k)),1)

def medved(x,y,n,a,b,c,l):
    #tusha
    ellipse(screen,(a,b,c), (x,y,int(260/n),int(450*k/n)),0)
    ellipse(screen,(0,0,0), (x,y,int(260/n),int(450*k/n)),1)

    ellipse(screen,(a,b,c), (x+int(140/n),y+int(320/n*k),int(190/n),int(150*k/n)),0)
    ellipse(screen,(0,0,0), (x+int(140/n),y+int(320/n*k),int(190/n),int(150*k/n)),1)

    ellipse(screen,(a,b,c), (x+int(255/n),y+int(440/n*k),int(140/n),int(50*k/n)),0)
    ellipse(screen,(0,0,0), (x+int(255/n),y+int(440/n*k),int(140/n),int(50*k/n)),1)

    ellipse(screen,(a,b,c), (x+int(210/n),y+int(100/n*k),int(115/n),int(50*k/n)),0)
    ellipse(screen,(0,0,0), (x+int(210/n),y+int(100/n*k),int(115/n),int(50*k/n)),1)

    ellipse(screen,(a,b,c), (x+int(130/n),y-int(70/n*k),int(180/n),int(95*k/n)),0)
    ellipse(screen,(0,0,0), (x+int(130/n),y-int(70/n*k),int(180/n),int(95*k/n)),1)
    #uchi
    circle(screen,(a,b,c), (x+int(155/n),y-int(50/n*k)),15/n)
    circle(screen,(0,0,0), (x+int(155/n),y-int(50/n*k)),15/n,1)
    #glaza
    circle(screen,(a,b,c), (x+int(210/n),y-int(35/n*k)),5)
    circle(screen,(0,0,0), (x+int(210/n),y-int(35/n*k)),5)
    #nos
    circle(screen,(a,b,c), (x+int(310/n),y-int(30/n*k)),5)
    circle(screen,(0,0,0), (x+int(310/n),y-int(30/n*k)),5)
    #rot
    line(screen,(0,0,0),(x+int(210/n),y),(x+int(270/n),y))
    line(screen,(0,0,0),(x+int(270/n),y),(x+int(308/n),y-int(18/n*k)),1)
    #ydochka
    line(screen,(0,0,0),(x+int(260/n),y+int((210)/n*k)),(x+int(289/n),y+int((210-55-8)/n*k)),5)
    line(screen,(0,0,0),(x+int(318/n),y+int(115/n*k)),(x+int(665/n),y-int(150/n*k)),5)
    line(screen,(0,0,0),(x+int(665/n),y-int(150/n*k)),(x+int(665/n)+5,y+int(400/n*k)-2+l),1)
    
def vedro(x,y):
    polygon(screen, (127,127,127),[(x-32,y),(x-20,y+85),(x-20+40,y+85),(x+32,y)],0)
    polygon(screen, (0,0,0),[(x-32,y),(x-20,y+85),(x-20+40,y+85),(x+32,y)],2)
    circle(screen, (0,0,0), (x,y-32),46,2)
    circle(screen, (230,230,230), (x,y-32),44,0)
    polygon(screen, (230,230,230),[(x-64,y),(x-64,y-80),(x+64,y-80),(x+64,y)],0)
    ellipse(screen, (0,0,0), (x-32,y-47,65,94),2)
    polygon(screen, (127,127,127),[(x-30,y+14),(x-20,y+85),(x+20,y+85),(x+30,y+14)],0)
    polygon(screen, (0,0,0),[(x-30,y+14),(x-20,y+85),(x+20,y+85),(x+30,y+14)],2)
    line(screen,(127,127,127),(x-29,y+14),(x+29,y+14),2)

    polygon(screen,(191,203,200), [(x-21.6,y+8),(x+20,y-30),(x,y+14)],0)
    polygon(screen,(0,0,0), [(x-21.6,y+8),(x+20,y-30),(x,y+14)],2)

    circle(screen, (0,0,0), (x,y-2),6)
    circle(screen, (121,121,242), (x,y-2),5)
    circle(screen, (126,132,140), (x+1,y-2),2)
    line(screen, (0,0,0),(x,y+14),(x+20,y-10),3)



k = 1000/1123

fon(0,0)
nebo(480,int(200*k))
luja(800-350,520+int(160*k),400,int(180*k))
medved(150,575-int(136*k),1.5,230,230,230,30)
vedro(600,900)
vedro(450,600)
medved(325,675,2.5,136,0,21,0)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
