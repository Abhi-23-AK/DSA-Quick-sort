def kth_largest(arr, k):
    n = len(arr)
    return kth_smallest(arr, 0, n - 1, n - k + 1)

arr = [12, 3, 5, 7, 4, 19, 26]
k = 2
print(f"{k}nd largest element is", kth_largest(arr, k))
# Output: 2nd largest element is 19