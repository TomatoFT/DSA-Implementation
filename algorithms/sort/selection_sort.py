from .base import BaseSort

class SelectionSort(BaseSort):
    def __init__(self):
        self.items = []

    def __init__(self, items):
        self.items = items

    def sort(self):
        n = len(self.items)

        for i in range (n):
            min_index = i
            for j in range (i + 1, n):
                if self.items[min_index] > self.items[j]:
                    min_index = j
            self.items[i], self.items[min_index] = self.swap(self.items[i], self.items[min_index])

     
    def display(self):
        print(self.items)

if __name__ == "__main__":
    selection_sort_instance = SelectionSort()

    # Example usage:
    unsorted_list = [64, 25, 12, 22, 11]
    selection_sort_instance.__add__(unsorted_list)

    print("Unsorted list:")
    selection_sort_instance.display()

    # Sorting the list using Selection Sort
    selection_sort_instance._SelectionSort__sort()

    print("\nSorted list:")
    selection_sort_instance.display()
