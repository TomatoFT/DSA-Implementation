from .base import BaseSort

class InsertionSort(BaseSort):
    def __init__(self, items) -> None:
        self.items = items

    def sort(self):
        n = len(self.items)
        for i in range(n):
            key = self.items[i]
            j = i - 1
            while (j >= 0 and self.items[j] > key):
                self.items[j+1], self.items[j] = self.swap(self.items[j+1], self.items[j])
                j = j - 1
    
    def display(self):
        print(self.items)