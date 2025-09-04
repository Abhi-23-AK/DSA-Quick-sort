'''If the array has lots of duplicates (e.g., [5,5,5,5,2,3]), normal QuickSort wastes time.
 3-way partition divides into < pivot, = pivot, > pivot in one pass.'''
def quicksort_3way(arr, low, high):
    if low >= high:
        return
    
    lt, i, gt = low, low, high
    pivot = arr[low]
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    quicksort_3way(arr, low, lt - 1)
    quicksort_3way(arr, gt + 1, high)

# ---------- Driver ----------
arr = [4, 9, 4, 4, 3, 7, 4, 9, 3]
quicksort_3way(arr, 0, len(arr) - 1)
print("Sorted array (3-way QuickSort):", arr)
# Output: Sorted array (3-way QuickSort): [3, 3, 4, 4, 4, 4, 7, 9, 9]