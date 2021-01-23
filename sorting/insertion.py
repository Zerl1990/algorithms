"""Insertion sort implementation."""
import random


def insertion_sort(arr: list) -> list:
    """Sort list of values using insertion sort algorithm

    :param arr: List of values
    :return: New list with numbers sorted
    """
    s_arr = arr.copy()
    for j in range(1, len(s_arr)):
        i = j - 1
        while i > 0 and s_arr[i] > s_arr[i+1]:
            print_sorting_progress(s_arr, i, i+1)
            s_arr[i], s_arr[i + 1] = s_arr[i+1], s_arr[i]
            i -= 1
    return s_arr


def print_sorting_progress(arr: list, *args):
    """Print sorting progress

    :param arr: Current results.
    :param args: List with index to highlight
    :return: None
    """
    values = []
    for index, value in enumerate(arr):
        value = str(value)
        if index in args:
            value = '[' + value + ']'
        value = value.rjust(6)
        values.append(value)
    print(' '.join(values))


if __name__ == '__main__':
    numbers = random.sample(range(0, 100), 10)
    numbers = insertion_sort(numbers)
