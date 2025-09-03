'''Worst-case O(n) selection (better than Randomized QuickSelect).
👉 Used in order statistics (like finding median or kth element).'''
def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    i = low
    for j in range(low, high):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def median_of_medians(arr, low, high, k):
    if low == high:
        return arr[low]
    
    n = high - low + 1
    medians = []
    
    for i in range(low, high + 1, 5):
        sub = arr[i:min(i+5, high+1)]
        sub.sort()
        medians.append(sub[len(sub)//2])
    
    if len(medians) == 1:
        median = medians[0]
    else:
        median = median_of_medians(medians, 0, len(medians)-1, len(medians)//2)
    
    pivot_index = arr.index(median)
    pos = partition(arr, low, high, pivot_index)
    
    if pos - low == k:
        return arr[pos]
    elif pos - low > k:
        return median_of_medians(arr, low, pos - 1, k)
    else:
        return median_of_medians(arr, pos + 1, high, k - (pos - low + 1))

# ---------- Driver ----------
arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
print(f"{k}rd smallest element is", median_of_medians(arr, 0, len(arr)-1, k-1))
# Output: 3rd smallest element is 5