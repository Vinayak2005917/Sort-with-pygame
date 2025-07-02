import time


#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                time.sleep(0.15)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                return arr  
            
#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            time.sleep(0.15)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



#Selection Sort, Merge Sort, and Quick Sort