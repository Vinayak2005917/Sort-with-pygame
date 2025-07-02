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

#Bubble sort button
bubble_sort_rect = pygame.Rect(0, 0, 150, 75)
bubble_sort_image = pygame.image.load("Bubble sort.png")
bubble_sort_image = pygame.transform.scale(bubble_sort_image, (150,75))
bubble_sort = False

#Insertion sort button
insertion_sort_rect = pygame.Rect(150, 0, 150, 75)
insertion_sort_image = pygame.image.load("Insertion sort.png")
insertion_sort_image = pygame.transform.scale(insertion_sort_image, (150,75))
inertion_sort = False




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
            if bubble_sort_rect.collidepoint(event.pos):
                if bubble_sort_rect.collidepoint(event.pos):
                    bubble_sort = True
                    print("Bubble sort button clicked!")
            elif insertion_sort_rect.collidepoint(event.pos):
                if insertion_sort_rect.collidepoint(event.pos):
                    inertion_sort = True
                    print("Insertion sort button clicked!")


    screen.fill((255,255,255))
    screen.blit(bubble_sort_image, bubble_sort_rect)
    screen.blit(insertion_sort_image, insertion_sort_rect)



    for i in range(20):
        bar_height = numbers[i]
        x = 10 + (i * 40)
        y = 595 - bar_height
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, bar_height))
    
    if bubble_sort:
        sorting_functions.bubble_sort(numbers)
    elif inertion_sort:
        sorting_functions.insertion_sort(numbers)

    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
