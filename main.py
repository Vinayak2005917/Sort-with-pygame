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


button_rect = pygame.Rect(0, 0, 150, 75)
button_image = pygame.image.load("Quick sort.png")
button_image = pygame.transform.scale(button_image, (150,75))
sort = False
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if button_rect.collidepoint(event.pos):
                    sort = True
                    print("Button clicked!")
    screen.fill((255,255,255))
    screen.blit(button_image, button_rect)



    for i in range(20):
        bar_height = numbers[i]
        x = 10 + (i * 40)
        y = 595 - bar_height
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, bar_height))
    
    if sort:
        sorting_functions.bubble_sort(numbers)
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
