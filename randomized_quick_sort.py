'''Normal QuickSort has worst-case O(n²) if the pivot is always bad (like sorted input).
👉 Randomized QuickSort picks a random pivot each time → average O(n log n) guaranteed.'''
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# ---------- Driver ----------
arr = [10, 7, 8, 9, 1, 5]
randomized_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array (Randomized QuickSort):", arr)
