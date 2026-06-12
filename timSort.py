MIN_MERGE = 32

def calc_min_run(n):
    "Calculates the minimum run length optimal for merging."
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    "Standard Inseration Sort to handle small sub-arrays (runs)."
    for i in range(left + 1, right +1):
        j = i
        while j > left and arr[j] < arr[j -1]:
            arr[j], arr[j -1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    "Merges two sorted adjacent runs."
    len1, len2 = m - l + 1, r - m
    left, right = [], []

    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

        while i < len1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len2:
            arr[k] = right[j]
            j += 1
            k += 1

def tim_sort(arr):
    "The main TimSort engine."
    n = len(arr)
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size -1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

if __name__ == "__main__":
    import random

    data = [random.randint(1, 1000) for _ in range(100)]

    print("Original Array (First 20 items): ")
    print(data[:20], "... \n")

    tim_sort(data)

    print("Sorted Array: ")
    print(data)
