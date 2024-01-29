from data_structure.stack.stack import Stack

class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.stack = Stack()

    def __call__(self, start):
        self.dfs_recursive(start)
        self.display_result()

    def dfs_recursive(self, start):
        if start not in self.stack.items:
            self.stack.push(start)

            for neighbor in self.graph.graph_dict.get(start, []):
                self.dfs_recursive(neighbor)

    def display_result(self):
        print("DFS traversal:")
        print("Visited nodes:", self.stack.items)