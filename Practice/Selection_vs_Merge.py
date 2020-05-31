import time
import random


def selection_sort(lst):
    if type(lst) == list:
        for i in range(len(lst) - 1):
            for j in range(i+1, len(lst)):
                if lst[j] < lst[i]:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    else:
        print("please use a list")


def avg(lst):
    return sum(lst) / len(lst)


selection_sort_times = []
merge_sort_times = []
for i in range(10):
    array = list(range(0, 1000))
    rng = random.Random()
    rng.shuffle(array)
    t0 = time.perf_counter()
    selection_sort(array)
    t1 = time.perf_counter()
    selection_sort_times.append(t1-t0)
    array = list(range(0, 1000))
    rng.shuffle(array)
    t2 = time.perf_counter()
    array.sort()
    t3 = time.perf_counter()
    merge_sort_times.append(t3-t2)
print("Average time of Selection sort: {:.4f} seconds".format(avg(selection_sort_times)))
print("Average time of Merge sort: {:.4f} seconds".format(avg(merge_sort_times)))
