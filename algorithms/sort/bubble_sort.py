from .base import BaseSort

class BubbleSort(BaseSort):
    def __init__(self):
        self.items = []

    def __init__(self, items):
        self.items = items

    def sort(self):
        for i in range(len(self.items)):
            for j in range(i + 1, len(self.items)):
                if self.items[i] > self.items[j]:
                    self.items[i], self.items[j] = self.swap(self.items[i], self.items[j])

    def display(self):
        print(self.items)

