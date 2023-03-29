import time
import matplotlib.pyplot as plt
import random
from sorts import selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort

def main():
    subjects = {}

    subjects["300, sorted"] = []
    for i in range(300):
        subjects["300, sorted"].append(i)
        
    subjects["300, random"] = []
    for i in range(300):
        r = random.randint(0, 100)
        subjects["300, random"].append(r)
    
    subjects["300, reverse sorted"] = []
    for i in range(300):
        subjects["300, reverse sorted"].append(300 - i)

    # subjects["1000, random"] = []
    # for i in range(1000):
    #     r = random.randint(0, 100)
    #     subjects["1000, random"].append(r)

    iterations = len(subjects)

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
    plt.title('Average (of %s) time to sort' %str(iterations))
    plt.plot(subjects.keys(), selection_sort_times, label = "selection sort average")
    plt.plot(subjects.keys(), insertion_sort_times, label = "insertion sort average")
    plt.plot(subjects.keys(), bubble_sort_times, label = "bubble sort average")
    plt.plot(subjects.keys(), merge_sort_times, label = "merge sort average")
    plt.plot(subjects.keys(), quick_sort_times, label = "quick sort average")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
