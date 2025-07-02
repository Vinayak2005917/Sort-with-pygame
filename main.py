import pygame
import sys
import random
import time
import sorting_functions


pygame.init()
WIDTH, HEIGHT = 800, 700
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
insertion_sort = False


#Timer
count = 0
timer_running = False
start_time = 0
font = pygame.font.SysFont(None, 48)
text_surface = font.render(f'Time = {count}', True, (0, 0, 0))
text_rect = text_surface.get_rect()
text_rect.topleft = (10, 85)




#this generates a list of random numbers
numbers = [random.randint(50, 500) for _ in range(25)]

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
                bubble_sort = True
                timer_running = True
                start_time = pygame.time.get_ticks()
                print("Bubble sort button clicked!")
                sort_generator = sorting_functions.bubble_sort(numbers)
            elif insertion_sort_rect.collidepoint(event.pos):
                insertion_sort = True
                timer_running = True
                start_time = pygame.time.get_ticks()
                print("Insertion sort button clicked!")
                sort_generator = sorting_functions.selection_sort(numbers)


    screen.fill((255,255,255))
    screen.blit(bubble_sort_image, bubble_sort_rect)
    screen.blit(insertion_sort_image, insertion_sort_rect)
    screen.blit(text_surface, text_rect) 



    for i in range(25):
        bar_height = numbers[i]
        x = 10 + (i * 31.6)
        y = 695 - bar_height
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, bar_height))





    if bubble_sort or insertion_sort:
        try:
            next(sort_generator)
        except StopIteration:
            timer_running = False
            bubble_sort = False
            insertion_sort = False
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            text_surface = font.render(f'Sorted in {elapsed_time:.2f} seconds', True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (10, 85)
    
        if timer_running:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            text_surface = font.render(f'Time = {elapsed_time:.2f}', True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (10, 85)
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
