
def selection_sort(unsorted: list) -> list:
    """Sorts an array using the selection sort algorithm.

    Args:
        arr (list): The array to sort.

    Returns:
        list: The sorted array.
    """
    # do not mutate unsorted
    sorted = unsorted.copy()
    for i in range(len(sorted)):
        min = i
        for j in range(i + 1, len(sorted)):
            if sorted[j] < sorted[min]:
                min = j
        sorted[i], sorted[min] = sorted[min], sorted[i]
    return sorted

def insertion_sort(unsorted: list) -> list:
    """Sorts an array using the insertion sort algorithm.

    Args:
        arr (list): The array to sort.

    Returns:
        list: The sorted array.
    """
    # do not mutate unsorted
    sorted = unsorted.copy()
    for i in range(1, len(sorted)):
        j = i
        while j > 0 and sorted[j - 1] > sorted[j]:
            sorted[j - 1], sorted[j] = sorted[j], sorted[j - 1]
            j -= 1
    return sorted

def bubble_sort(unsorted: list) -> list:
    """Sorts an array using the bubble sort algorithm.

    Args:
        arr (list): The array to sort.

    Returns:
        list: The sorted array.
    """
    sorted = unsorted.copy()
    for i in range(len(sorted)):
        for j in range(len(sorted) - 1):
            if sorted[j] > sorted[j + 1]:
                sorted[j], sorted[j + 1] = sorted[j + 1], sorted[j]
    return sorted

def merge(left: list, right: list) -> list:
    """Merges two sorted arrays into one sorted array.

    Args:
        left (list): The first sorted array.
        right (list): The second sorted array.

    Returns:
        list: The merged sorted array.
    """
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    if len(left) > 0:
        merged.extend(left)
    else:
        merged.extend(right)
    return merged

def merge_sort(unsorted: list) -> list:
    """Sorts an array using the merge sort algorithm.

    Args:
        arr (list): The array to sort.

    Returns:
        list: The sorted array.
    """
    if len(unsorted) <= 1:
        return unsorted
    mid = len(unsorted) // 2
    left = merge_sort(unsorted[:mid])
    right = merge_sort(unsorted[mid:])
    return merge(left, right)

def quick_sort(unsorted: list) -> list:
    """Sorts an array using the quick sort algorithm.

    Args:
        arr (list): The array to sort.

    Returns:
        list: The sorted array.
    """
    if len(unsorted) <= 1:
        return unsorted
    pivot = unsorted[0]
    left = []
    right = []
    for i in range(1, len(unsorted)):
        if unsorted[i] < pivot:
            left.append(unsorted[i])
        else:
            right.append(unsorted[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
