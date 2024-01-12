import random
import timeit
from numpy import number
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from timsort import timsort

EXECUTION_QTY = 100


def generate_half_sorted_list(size):
    half_size = size // 2
    sorted_half = list(range(half_size))
    random_half = random.sample(range(half_size, size), half_size)
    return sorted_half + random_half


def get_random_data(rangeStart: number, rangeEnd: number, qty: number):
    return [random.randint(rangeStart, rangeEnd) for _ in range(qty)]


def get_fastest_sort_alg(list: [number], list_title: str):
    results = {
        "Insertion Sort": timeit.timeit(
            lambda: insertion_sort(list.copy()), number=EXECUTION_QTY
        ),
        "Merge Sort": timeit.timeit(
            lambda: merge_sort(list.copy()), number=EXECUTION_QTY
        ),
        "Timsort": timeit.timeit(lambda: timsort(list.copy()), number=EXECUTION_QTY),
    }

    print(f"{list_title} list test: ".upper())

    for algorithm, execution_time in results.items():
        print(f"Algorithm: {algorithm}, Execution Time: {execution_time}")

    min_time_algorithm, min_time = min(results.items(), key=lambda x: x[1])

    print(
        f"Fastest sorting algorithm for {list_title} list is {min_time_algorithm} with result: {min_time}\n"
    )

    return min_time_algorithm, min_time


def determine_overal_champion(champions):
    champion_counts = {}
    for champion, _ in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return max(champion_counts, key=champion_counts.get)
