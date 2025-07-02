import time

def quick_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                time.sleep(0.1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                return arr  