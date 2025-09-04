# Quick Sort in Python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[-1]  # Choosing last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Driver code
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
print("Sorted array (Quick Sort):", quick_sort(arr))
