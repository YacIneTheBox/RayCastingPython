import math
import pygame
import sys
from shapely.geometry import LineString, Polygon
pygame.init()

w,h = 800,600
color=(0,0,0)
color1=(255,0,0)

startp=(50,50)

endp=(200,200)


square_rect = pygame.Rect(420, 100, 10, 5)


screen=pygame.display.set_mode((w,h))

pygame.display.set_caption("RayCast")

wall1 = (startp[0], startp[1], endp[0], endp[1])
lwall1 = LineString([(startp[0], startp[1]), (endp[0], endp[1])])
wall2= (900,200,400,150)
lwall2= LineString([(wall2[0],wall1[1]),(wall2[2],wall2[3])])



# boucle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # the game
    mouse_x,mouse_y=pygame.mouse.get_pos()

    ray1 = (square_rect.centerx, square_rect.centery, mouse_x, mouse_y)
    lray1= LineString([(square_rect.centerx, square_rect.centery), (mouse_x, mouse_y)])

    ray2 = (square_rect.centerx, square_rect.centery, mouse_x+5, mouse_y+5)
    lray2= LineString([(square_rect.centerx, square_rect.centery), (mouse_x+5, mouse_y+5)])

    ray3 = (square_rect.centerx, square_rect.centery, mouse_x - 5, mouse_y - 5)
    lray3 = LineString([(square_rect.centerx, square_rect.centery), (mouse_x - 5, mouse_y - 5)])

    ray4 = (square_rect.centerx, square_rect.centery, mouse_x + 10, mouse_y - 10)
    lray4 = LineString([(square_rect.centerx, square_rect.centery), (mouse_x + 10, mouse_y - 10)])

    ray5 = (square_rect.centerx, square_rect.centery, mouse_x - 10, mouse_y + 10)
    lray5 = LineString([(square_rect.centerx, square_rect.centery), (mouse_x - 10, mouse_y + 10)])

    ray6 = (square_rect.centerx, square_rect.centery, mouse_x + 15, mouse_y - 15)
    lray6 = LineString([(square_rect.centerx, square_rect.centery), (mouse_x + 15, mouse_y - 15)])

    ray7 = (square_rect.centerx, square_rect.centery, mouse_x - 15, mouse_y + 15)
    lray7 = LineString([(square_rect.centerx, square_rect.centery), (mouse_x - 15, mouse_y + 15)])

    lrays=(lray1,lray2,lray3,lray4,lray5,lray6,lray7)
    #dessin

    screen.fill((255,255,255))

    pygame.draw.line(screen,color,startp,endp,2)
    pygame.draw.line(screen, color,(wall2[0],wall1[1]),(wall2[2],wall2[3]), 2)

    pygame.draw.rect(screen, color, square_rect)

    i=0
    for i in range(7):
        if lrays[i].intersects(lwall1):
            intersection=lrays[i].intersection(lwall1)
            if intersection.geom_type == 'Point':
                intersection_point = (int(intersection.x),int(intersection.y))
                print(print(f"Collision detected at point: {intersection_point}"))
                pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 2)
        elif lrays[i].intersects(lwall2):
            intersection=lrays[i].intersection(lwall2)
            if intersection.geom_type == 'Point':
                intersection_point = (int(intersection.x),int(intersection.y))
                print(print(f"Collision detected at point: {intersection_point}"))
                pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 2)
        else:
            pygame.draw.line(screen, color1, square_rect.center, (mouse_x, mouse_y), 2)




    pygame.display.flip()
    pygame.time.Clock().tick(60)