import time
import matplotlib.pyplot as plt
import random
from sorts import selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort

def main():

    amt = 700


    subjects = {}
    key = "%s, sorted" %(str(amt))
    subjects[key] = []
    for i in range(amt):
        subjects[key].append(i)

    key = "%s, random" %(str(amt))
    subjects[key] = []
    for i in range(amt):
        r = random.randint(0, 2000)
        subjects[key].append(r)
    
    key = "%s, reverse sorted" %(str(amt))
    subjects[key] = []
    for i in range(amt):
        subjects[key].append(amt - i)
            
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
    plt.title('Large varying inputs of size %s' %(str(amt)))
    plt.plot(subjects.keys(), selection_sort_times, label = "selection sort average")
    plt.plot(subjects.keys(), insertion_sort_times, label = "insertion sort average")
    plt.plot(subjects.keys(), bubble_sort_times, label = "bubble sort average")
    plt.plot(subjects.keys(), merge_sort_times, label = "merge sort average")
    plt.plot(subjects.keys(), quick_sort_times, label = "quick sort average")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
