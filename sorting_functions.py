import time


#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                time.sleep(0.15)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                return arr  
            
#Insertion Sort, Selection Sort, Merge Sort, and Quick Sort