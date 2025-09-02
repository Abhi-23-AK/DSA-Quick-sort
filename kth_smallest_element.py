'''Find the Kth Smallest Element using QuickSort Partition

We use the partition logic (like QuickSelect). Instead of sorting the whole array, we only focus on the side where the kth element lies.'''
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def kth_smallest(arr, low, high, k):
    if 0 < k <= high - low + 1:
        pos = partition(arr, low, high)

        if pos - low == k - 1:
            return arr[pos]  # kth element found
        elif pos - low > k - 1:
            return kth_smallest(arr, low, pos - 1, k)
        else:
            return kth_smallest(arr, pos + 1, high, k - pos + low - 1)

# ---------- Driver Code ----------
arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
print(f"{k}rd smallest element is", kth_smallest(arr, 0, len(arr) - 1, k))
# Output: 3rd smallest element is 5