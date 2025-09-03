def partition(arr, low, high):
    """
    This function takes the last element as pivot,
    places the pivot at its correct position in sorted array,
    and places all smaller elements to the left of pivot
    and greater elements to the right of pivot.
    """
    pivot = arr[high]   # pivot element
    i = low - 1         # index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    
    # Place pivot in the right position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # return pivot index


def quick_sort(arr, low, high):
    """
    The main function that implements QuickSort.
    """
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ---------- Driver Code ----------
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
