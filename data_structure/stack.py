class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# # Example usage of the stack:
# if __name__ == "__main__":
#     stack = Stack()

#     # Push elements onto the stack
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)

#     # Print the top element (without removing it)
#     print("Top element:", stack.peek())

#     # Pop elements from the stack
#     while not stack.is_empty():
#         print("Popped:", stack.pop())

#     # Attempting to pop from an empty stack will raise an exception
#     # print(stack.pop())  # Uncomment to see the exception
