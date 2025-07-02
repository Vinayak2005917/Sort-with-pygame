import time


#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                time.sleep(0.15)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield 
            
#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            time.sleep(0.15)
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
            time.sleep(0.15)
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield
        


# #Merge Sort, and Quick Sort