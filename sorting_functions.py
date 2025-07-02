import time
import pygame
#sound effect
pygame.mixer.init()
pygame.mixer.music.load('mixkit-camera-shutter-click-1133.wav')
pygame.mixer.music.set_volume(0.5)

#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                time.sleep(0.05)
                pygame.mixer.music.play(0)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield 
            
#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            time.sleep(0.05)
            pygame.mixer.music.play(0)
            arr[j + 1] = arr[j]
            j -= 1
            yield
        arr[j + 1] = key



#Selection Sort 
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            time.sleep(0.05)
            pygame.mixer.music.play(0)
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield
        


# #Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        yield from merge_sort(L)
        yield from merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            yield

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            yield

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            yield




# Quick Sort
def quick_sort(arr, low, high):
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            yield
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            time.sleep(0.05)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
