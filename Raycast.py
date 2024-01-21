import math
import pygame
import sys
from shapely.geometry import LineString
import random

pygame.init()

w, h = 800, 600

color = (255, 255, 255)

startp = (50, 50)

endp = (200, 200)

square_rect = pygame.Rect(420, 100, 10, 5)

screen = pygame.display.set_mode((w, h))

pygame.display.set_caption("RayCast")

wall1 = (startp[0], startp[1], endp[0], endp[1])
lwall1 = LineString([(startp[0], startp[1]), (endp[0], endp[1])])
wall2 = (900, 200, 400, 150)
lwall2 = LineString([(wall2[0], wall2[1]), (wall2[2], wall2[3])])
wall3 = (600, 500, 300, 400)
lwall3 = LineString([(wall3[0], wall3[1]), (wall3[2], wall3[3])])
wall4 = (300, 600, 100, 300)
lwall4 = LineString([(wall4[0], wall4[1]), (wall4[2], wall4[3])])
line_length = 1000

lwalls = [lwall1, lwall2, lwall3, lwall4]
walls = [wall1, wall2, wall3, wall4]
# boucle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # the game
    #color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color1 = (194, 194, 6)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    square_rect.x = mouse_x - square_rect.width / 2
    square_rect.y = mouse_y - square_rect.height / 2

    # dessin

    screen.fill((54, 59, 58))

    pygame.draw.line(screen, color, startp, endp, 2)
    pygame.draw.line(screen, color, (wall2[0], wall2[1]), (wall2[2], wall2[3]), 2)
    pygame.draw.line(screen, color, (wall3[0], wall3[1]), (wall3[2], wall3[3]), 2)
    pygame.draw.line(screen, color, (wall4[0], wall4[1]), (wall4[2], wall4[3]), 2)

    pygame.draw.rect(screen, color, square_rect)

    # creation of the rays
    i = 0
    for i in range(360):
        angle_degree = i
        angle_radians = math.radians(angle_degree)
        end_point = (
            square_rect.centerx + int(line_length * math.cos(angle_radians)),
            square_rect.centery + int(line_length * math.sin(angle_radians))
        )
        lray = LineString([(square_rect.x, square_rect.y), end_point])
        z = 0
        intersection_point = end_point
        mini = math.sqrt((mouse_x - wall2[0]) ** 2 + (mouse_y - wall2[1]) ** 2)
        cmpt = 0
        # boucle de checking de wall chaque ray est test avec tous les wall
        distance_wall = []

        # detecter quel wall est le plus proche
        for j in range(len(lwalls)):
            midpointx = ((walls[j][0] + walls[j][2])/2)
            midpointy = ((walls[j][1] + walls[j][2])/2)
            distance_wall.append(math.sqrt((mouse_x - midpointx) ** 2 + (mouse_y - midpointy) ** 2))


        valeur_minimale = min(distance_wall)
        closest = distance_wall.index(valeur_minimale)
        lwalls[0], lwalls[closest] = lwalls[closest], lwalls[0]
        walls[0], walls[closest] = walls[closest], walls[0]

        for z in range(len(lwalls)):

            j = 0
            if lray.intersects(lwalls[z]):
                intersection = lray.intersection(lwalls[z])
                cmpt += 1
                if intersection.geom_type == 'Point':
                    intersection_point = (int(intersection.x), int(intersection.y))
                    break

        pygame.draw.line(screen, color1, square_rect.center, (intersection_point[0], intersection_point[1]), 1)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
