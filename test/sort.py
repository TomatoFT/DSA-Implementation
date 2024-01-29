import sys

sys.path.append('./')

from algorithms.sort.bubble_sort import BubbleSort
from algorithms.sort.selection_sort import SelectionSort

if __name__ == "__main__":

    # Example usage:
    unsorted_list = [64, 25, 12, 22, 11]

    # sort_algorithms = BubbleSort(unsorted_list)
    sort_algorithms = SelectionSort(unsorted_list)


    print("Unsorted list:")
    sort_algorithms.display()

    # Sorting the list using Bubble Sort
    sort_algorithms.sort()

    print("\nSorted list:")
    sort_algorithms.display()