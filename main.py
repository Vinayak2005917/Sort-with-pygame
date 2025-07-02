import pygame
import sys
import random
import time
import sorting_functions

pygame.init()
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Sorting Algorithms Visualizer with Audio")
clock = pygame.time.Clock()
FPS = 60

#Bubble sort button
bubble_sort_rect = pygame.Rect(0, 0, 150, 75)
bubble_sort_image = pygame.image.load("Button images/Bubble sort.png")
bubble_sort_image = pygame.transform.scale(bubble_sort_image, (150,75))
bubble_sort = False

#Insertion sort button
insertion_sort_rect = pygame.Rect(150, 0, 150, 75)
insertion_sort_image = pygame.image.load("Button images/Insertion sort.png")
insertion_sort_image = pygame.transform.scale(insertion_sort_image, (150,75))
insertion_sort = False

#Selection sort button
selection_sort_rect = pygame.Rect(300, 0, 150, 75)
selection_sort_image = pygame.image.load("Button images/Selection sort.png")
selection_sort_image = pygame.transform.scale(selection_sort_image, (150,75))
selection_sort = False

#Quick sort button
quick_sort_rect = pygame.Rect(450, 0, 150, 75)
quick_sort_image = pygame.image.load("Button images/Quick sort.png")
quick_sort_image = pygame.transform.scale(quick_sort_image, (150,75))
quick_sort = False

# Merge sort button
merge_sort_rect = pygame.Rect(600, 0, 150, 75)
merge_sort_image = pygame.image.load("Button images/Merge sort.png")
merge_sort_image = pygame.transform.scale(merge_sort_image, (150,75))
merge_sort = False

#Reset button
reset_rect = pygame.Rect(750, 0, 150, 75)
reset_image = pygame.image.load("Button images/Reset.png")
reset_image = pygame.transform.scale(reset_image, (150,75))



#Timer
count = 0
timer_running = False
start_time = 0
font = pygame.font.SysFont(None, 48)
text_surface = font.render(f'Time = {count}', True, (0, 0, 0))
text_rect = text_surface.get_rect()
text_rect.topleft = (0, 85)



number_of_bars = 40
#this generates a list of random numbers
numbers = [random.randint(50, 500) for _ in range(number_of_bars)]

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
                sort_generator = sorting_functions.insertion_sort(numbers)
            elif selection_sort_rect.collidepoint(event.pos):
                selection_sort = True
                timer_running = True
                start_time = pygame.time.get_ticks()
                print("Selection sort button clicked!")
                sort_generator = sorting_functions.selection_sort(numbers)
            elif quick_sort_rect.collidepoint(event.pos):
                quick_sort = True
                timer_running = True
                start_time = pygame.time.get_ticks()
                print("Quick sort button clicked!")
                sort_generator = sorting_functions.quick_sort(numbers, 0, len(numbers) - 1)
            elif merge_sort_rect.collidepoint(event.pos):
                merge_sort = True
                timer_running = True
                start_time = pygame.time.get_ticks()
                print("Merge sort button clicked!")
                sort_generator = sorting_functions.merge_sort(numbers)
            elif reset_rect.collidepoint(event.pos):
                bubble_sort = False
                insertion_sort = False
                selection_sort = False
                quick_sort = False
                merge_sort = False
                timer_running = False
                numbers = [random.randint(50, 500) for _ in range(number_of_bars)]
                start_time = 0
                text_surface = font.render(f'Time = {count}', True, (0, 0, 0))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (10, 85)
                print("Reset button clicked!")


    screen.fill((255,255,255))
    screen.blit(bubble_sort_image, bubble_sort_rect)
    screen.blit(insertion_sort_image, insertion_sort_rect)
    screen.blit(selection_sort_image, selection_sort_rect)
    screen.blit(quick_sort_image, quick_sort_rect)
    screen.blit(merge_sort_image, merge_sort_rect)
    screen.blit(reset_image, reset_rect)
    screen.blit(text_surface, text_rect) 



    sorted_numbers = sorted(numbers)  # Keep this OUTSIDE the loop
    for i in range(number_of_bars):
        bar_height = numbers[i]
        x = 10 + (i * 29.8)
        y = 695 - bar_height
        if numbers[i] == sorted_numbers[i]:
            color = (0, 190, 0)
        elif numbers[i] - sorted_numbers[i] < 15:
            color = (225, 80, 8)
        elif numbers[i] - sorted_numbers[i] < 1:
            color = (225, 10, 8)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(screen, color, (x, y, 20, bar_height))


    if bubble_sort or insertion_sort or selection_sort or quick_sort or merge_sort:
        try:
            next(sort_generator)
        except StopIteration:
            timer_running = False
            bubble_sort = False
            insertion_sort = False
            selection_sort = False
            quick_sort = False
            merge_sort = False
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