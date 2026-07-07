## Selection sort - relies on Employee's __lt__, which compares by hourly_salary


def selection_sort(items):
    n = len(items)

    for i in range(n - 1):
        # assume position i already holds the smallest remaining item
        smallest_index = i

        # scan the rest of the list for anything smaller
        for j in range(i + 1, n):
            if items[j] < items[smallest_index]:
                smallest_index = j

        # swap the smallest found into position i, if needed
        if smallest_index != i:
            items[i], items[smallest_index] = items[smallest_index], items[i]

    return items
