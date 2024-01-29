from data_structure.queue.queue import Queue

class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.queue = Queue()

    def __call__(self, start):
        self.queue.enqueue(start)
        visited = []

        while not self.queue.is_empty():
            current_vertex = self.queue.dequeue()
            print(current_vertex)
            if current_vertex not in visited:
                visited.append(current_vertex)
                for neighbor in self.graph.graph_dict.get(current_vertex, []):
                    self.queue.enqueue(neighbor)
        self.display_result(visited)

    @staticmethod
    def display_result(visited):
        print("BFS traversal:")
        print("Visited nodes:", visited)