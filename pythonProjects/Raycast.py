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
wall = LineString([(startp[0], startp[1]), (endp[0], endp[1])])



# boucle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # the game
    mouse_x,mouse_y=pygame.mouse.get_pos()
    ray1 = (square_rect.centerx, square_rect.centery, mouse_x, mouse_y)
    ray= LineString([(square_rect.centerx, square_rect.centery), (mouse_x, mouse_y)])

    #dessin

    screen.fill((255,255,255))

    pygame.draw.line(screen,color,startp,endp,2)

    pygame.draw.rect(screen, color, square_rect)



    if ray.intersects(wall):
        intersection=ray.intersection(wall)
        if intersection.geom_type == 'Point':
            intersection_point = (int(intersection.x),int(intersection.y))
            print(print(f"Collision detected at point: {intersection_point}"))
            pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 2)
    else:
        pygame.draw.line(screen, color1, square_rect.center, (mouse_x, mouse_y), 2)



    pygame.display.flip()
    pygame.time.Clock().tick(60)