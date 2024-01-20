import math
import pygame
import sys
from shapely.geometry import LineString, Polygon
pygame.init()

w,h = 800,600
color=(255,255,255)
color1=(255,255,255)

startp=(50,50)

endp=(200,200)


square_rect = pygame.Rect(420, 100, 10, 5)


screen=pygame.display.set_mode((w,h))

pygame.display.set_caption("RayCast")

wall1 = (startp[0], startp[1], endp[0], endp[1])
lwall1 = LineString([(startp[0], startp[1]), (endp[0], endp[1])])
wall2= (900,200,400,150)
lwall2= LineString([(wall2[0],wall2[1]),(wall2[2],wall2[3])])
wall3= (600,500,300,600)
lwall3= LineString([(wall3[0],wall3[1]),(wall3[2],wall3[3])])

line_length = 1000


# boucle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # the game
    mouse_x,mouse_y=pygame.mouse.get_pos()
    square_rect.x = mouse_x - square_rect.width / 2
    square_rect.y = mouse_y - square_rect.height / 2

    #dessin

    screen.fill((0,0,0))

    pygame.draw.line(screen,color,startp,endp,2)
    pygame.draw.line(screen, color,(wall2[0],wall2[1]),(wall2[2],wall2[3]), 2)
    pygame.draw.line(screen,color,(wall3[0],wall3[1]),(wall3[2],wall3[3]),2)

    pygame.draw.rect(screen, color, square_rect)


    # creation of the rays
    i=0
    for i in range(360):
        angle_degree=i
        angle_radians=math.radians(angle_degree)
        end_point = (
            square_rect.centerx + int(line_length * math.cos(angle_radians)),
            square_rect.centery + int(line_length * math.sin(angle_radians))
        )
        lray=LineString([(square_rect.centerx,square_rect.centery),end_point])

        if lray.intersects(lwall1):
            intersection=lray.intersection(lwall1)
            if intersection.geom_type == 'Point':
                intersection_point = (int(intersection.x),int(intersection.y))
                print(print(f"Collision detected at point: {intersection_point}"))
                pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 1)
        elif lray.intersects(lwall2):
            intersection=lray.intersection(lwall2)
            if intersection.geom_type == 'Point':
                intersection_point = (int(intersection.x),int(intersection.y))
                print(print(f"Collision detected at point: {intersection_point}"))
                pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 1)
        elif lray.intersects(lwall3):
            intersection=lray.intersection(lwall3)
            if intersection.geom_type == 'Point':
                intersection_point = (int(intersection.x),int(intersection.y))
                print(print(f"Collision detected at point: {intersection_point}"))
                pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 1)
        else:
            pygame.draw.line(screen, color1, square_rect.center, end_point, 1)

    pygame.display.flip()
    pygame.time.Clock().tick(60)