#controls, left click to draw points
#space to finish shape
#esc to get coords

import os
import pygame
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (900,200)
pygame.init()
screen = pygame.display.set_mode((400,400))
#font3 = pygame.font.Font('freesansbold.ttf', 24)
colors = [(255,255,255)]
polygons = [[]]
target = 0
shrink_ratio = 5

def process_polygons(polys):
    newnew = []
    for i in polys:
        new = []
        for j in i:
            new.append((round(j[0]/shrink_ratio),round(j[1]/shrink_ratio)))
        newnew.append(new)
    for i in newnew:
        print (i)
    
while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            polygons[target].append(pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            try:
                polygons[target].pop()
            except:
                pass
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    target += 1
                    polygons.append([])
                    colors.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                elif event.key == pygame.K_ESCAPE:
                    process_polygons(polygons)
    try:
        for i in range (len(polygons)):
            try:
                pygame.draw.line(screen,colors[i],polygons[target][i],polygons[target][-1])
            except:
                pass
    except:
        pass
    try:
        for i in range (len(polygons)):
            try:
                pygame.draw.polygon(screen,colors[i],polygons[i])
            except:
                pass
    except:
        pass
    if len (polygons[target]) > 0:
        pygame.draw.line(screen,colors[i],polygons[target][-1],pos)
    try:
        pygame.draw.polygon(screen,colors[i],polygons[i])
    except:
        pass
    polygons[i].append(pos)
    try:
        pygame.draw.polygon(screen,colors[i],polygons[i])
    except:
        pass
    del polygons[i][-1]
    pygame.display.update()