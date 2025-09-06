'''Helps reduce recursion depth by always recursing on the smaller subarray first (turns tail recursion into a loop).'''
def tail_recursive_quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        
        # Recurse on smaller side first
        if pi - low < high - pi:
            tail_recursive_quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            tail_recursive_quick_sort(arr, pi + 1, high)
            high = pi - 1

# ---------- Driver ----------
arr = [10, 7, 8, 9, 1, 5]
tail_recursive_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array (Tail Recursive QuickSort):", arr)
# Output: Sorted array (Tail Recursive QuickSort): [1, 5, 7, 8, 9, 10]