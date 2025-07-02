import pygame
import sys
import random
import time
import sorting_functions


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Pygame Basic Setup")
clock = pygame.time.Clock()
FPS = 60


#this generates a list of random numbers
numbers = [random.randint(50, 500) for _ in range(20)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    screen.fill((255,255,255))



    for i in range(20):
        bar_height = numbers[i]
        x = 10 + (i * 40)
        y = 550 - bar_height
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, bar_height))
     
    quick_sort(numbers)
    
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
