## Quicksort - takes a key function so it can sort by anything.
## For this assignment: quick_sort(employees, key=Employee.name_key)


def quick_sort(items, key=lambda item: item):
    _quick_sort(items, 0, len(items) - 1, key)
    return items


def _quick_sort(items, low, high, key):
    if low < high:
        pivot_index = _partition(items, low, high, key)
        _quick_sort(items, low, pivot_index - 1, key)
        _quick_sort(items, pivot_index + 1, high, key)


def _partition(items, low, high, key):
    pivot = key(items[high])  # last element as pivot
    i = low - 1  # tracks last index of something smaller than pivot

    for j in range(low, high):
        if key(items[j]) < pivot:
            i += 1
            items[i], items[j] = items[j], items[i]

    items[i + 1], items[high] = items[high], items[i + 1]
    return i + 1