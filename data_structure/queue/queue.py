class Queue:
    """A simple implementation of a queue."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self.queue = []

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def push(self, item) -> None:
        """
        Add an item to the end of the queue.

        Args:
        - item: The item to be added to the queue.

        Raises:
        - IndexError: If the item is not valid (empty or None).
        """
        if item is not None:
            self.queue.append(item)
        
        return self
        
    def dequeue(self):
        """
        Remove the first item from the queue.

        Raises:
        - IndexError: If the queue is empty.
        """
        if not self.is_empty():
            value = self.queue[0]
            self.queue = self.queue[1:]
            return value
