import random

def bubble_sort(arr, comparison_function):
    swaps = 0
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                sorted_flag = False
                swaps += 1
    print(f"Bubble sort: There were {swaps} swaps")
    return arr

def quicksort(lst, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = lst[pivot_idx]
    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, lst[i]):
            lst[i], lst[less_than_pointer] = lst[less_than_pointer], lst[i]
            less_than_pointer += 1
    lst[end], lst[less_than_pointer] = lst[less_than_pointer], lst[end]
    quicksort(lst, start, less_than_pointer - 1, comparison_function)
    quicksort(lst, less_than_pointer + 1, end, comparison_function)
