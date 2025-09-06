'''Sort an Array of 0s, 1s, and 2s (Dutch National Flag using QuickSort Idea)'''
def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# ---------- Driver ----------
arr = [0, 1, 2, 1, 0, 1, 2, 1, 0]
print("Sorted 0/1/2:", sort_012(arr))
# Output: Sorted 0/1/2: [0, 0, 0, 1, 1, 1, 1, 2, 2]