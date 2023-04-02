import time
import matplotlib.pyplot as plt
from sorts import selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort

def main():
    subjects = {
        "empty list": [],
        "one element": [1],
        "sorted": [1, 2, 3],
        "duplicates": [1, 3, 3],
        "10, sorted": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "10, reverse sorted": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        "10, unsorted": [5, 4, 3, 2, 1, 6, 7, 8, 9, 0], # ten elements, unsorted, unique
        "10, unsorted duplicates": [1, 3, 2, 3, 4, 5, 6, 5, 2, 5], # ten elements, unsorted with duplicates
        "20, unsorted": [5, 4, 3, 2, 1, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], # twenty elements, unsorted, unique
    }

    selection_sort_times = []
    for subject in subjects.values():
        start = time.time()
        selection_sort(subject)
        end = time.time()
        selection_sort_times.append(end - start)

    insertion_sort_times = []
    for subject in subjects.values():
        start = time.time()
        insertion_sort(subject)
        end = time.time()
        insertion_sort_times.append(end - start)
    
    bubble_sort_times = []
    for subject in subjects.values():
        start = time.time()
        bubble_sort(subject)
        end = time.time()
        bubble_sort_times.append(end - start)

    merge_sort_times = []
    for subject in subjects.values():
        start = time.time()
        merge_sort(subject)
        end = time.time()
        merge_sort_times.append(end - start)

    quick_sort_times = []
    for subject in subjects.values():
        start = time.time()
        quick_sort(subject)
        end = time.time()
        quick_sort_times.append(end - start)

    # draw graph
    # x axis is indices of subjects
    # y axis is selection_sort_times
    plt.xticks(rotation = 60)
    plt.title('Time to sort with different inputs')
    plt.plot(subjects.keys(), selection_sort_times, label = "selection sort average")
    plt.plot(subjects.keys(), insertion_sort_times, label = "insertion sort average")
    plt.plot(subjects.keys(), bubble_sort_times, label = "bubble sort average")
    plt.plot(subjects.keys(), merge_sort_times, label = "merge sort average")
    plt.plot(subjects.keys(), quick_sort_times, label = "quick sort average")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
