import pygame
import math
from config import *


pygame.init()

WIDTH = int(Height * Aspect_ratio)

if Circle_grow_effect_enabled:
    radius_cahnger = 3.5
else:
    radius_cahnger = 2.5

ball_x = WIDTH // 2  
ball_y = Height // 3  
ball_speed = 5  

circle_center = (WIDTH // 2, Height // 2)
circle_radius = min(WIDTH, Height) // radius_cahnger 

gravity = Gravity

ball_angle = math.pi / 3  
ball_dx = ball_speed * math.cos(ball_angle)
ball_dy = ball_speed * math.sin(ball_angle)

screen = pygame.display.set_mode((WIDTH, Height))
pygame.display.set_caption('ball bouncing sim')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_dx
    ball_y += ball_dy
    
    ball_dy += gravity
    
    dist_to_center = math.sqrt((ball_x - circle_center[0])**2 + (ball_y - circle_center[1])**2)
    if dist_to_center >= circle_radius - Ball_size:

        normal_angle = math.atan2(ball_y - circle_center[1], ball_x - circle_center[0])
        incident_angle = math.atan2(ball_dy, ball_dx)
        reflection_angle = 2 * normal_angle - incident_angle + math.pi  # reflection angle formula

        ball_dx = ball_speed * math.cos(reflection_angle)
        ball_dy = ball_speed * math.sin(reflection_angle)

        if Ball_grow_effect_enabled:
            Ball_size += effect_strenght
        if Ball_shrink_effect_enabled:
            Ball_size -= effect_strenght

        if Circle_shrink_effect_enabled:
            radius_cahnger += effect_strenght * 0.05
            circle_radius = min(WIDTH, Height) // radius_cahnger 
        if Circle_grow_effect_enabled:
            radius_cahnger -= effect_strenght * 0.05
            circle_radius = min(WIDTH, Height) // radius_cahnger
        
        # Adjust ball position to stay on the circle's boundary
        ball_x = circle_center[0] + (circle_radius - Ball_size) * math.cos(normal_angle)
        ball_y = circle_center[1] + (circle_radius - Ball_size) * math.sin(normal_angle)

    screen.fill(backgroundcolor)

    pygame.draw.circle(screen, ballcolor, (int(ball_x), int(ball_y)), Ball_size)

    pygame.draw.circle(screen, circlecolor, circle_center, circle_radius, Circle_thickness)
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

pygame.quit()
