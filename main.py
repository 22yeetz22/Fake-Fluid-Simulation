import pygame
from particle import Droplet
from random import randint
from numpy import array

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fake Fluid Simulation")

DT = 2  # Delta time (amount of extra time for a frame)
N_BALLS = 200
MOUSE_SIZE = 30

# Generate n balls at random positions
balls = array([Droplet(randint(50, 750), randint(25, 320), randint(20, 30)) for _ in range(N_BALLS)])

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Background is white

    # Calculate ball collision with every ball possible (slow)
    for b1 in balls:
        for b2 in balls:
            if b1 != b2:
                b1.colliding(b2, DT)

    # Draw balls and update their position
    for ball in balls:
        ball.update_position()
        ball.draw(screen)

    # Create mouse collider
    mousepos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (65, 102, 245), mousepos, MOUSE_SIZE)

    # Update screen
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
