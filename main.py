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

    # draw graph
    # x axis is indices of subjects
    # y axis is selection_sort_times
    plt.xticks(rotation = 45)
    plt.plot(subjects.keys(), selection_sort_times)
    plt.show()


if __name__ == '__main__':
    main()
