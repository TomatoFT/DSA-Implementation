from abc import ABC, abstractmethod

class BaseSort(ABC):
    @abstractmethod
    def __init__(self, items) -> None:
        super().__init__()

    @staticmethod
    def swap(a,b):
        temp = a
        a = b
        b = temp

        return a, b
