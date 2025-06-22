def bubblesort(n):
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            flag = True
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    flag = False
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if flag:
                break
                
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # already sorted
    pivot = arr[len(arr) // 2]  # pick middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

