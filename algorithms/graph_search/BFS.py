from data_structure.queue.queue import Queue

def bfs(graph, start):
    queue = Queue().push(start)
    visited = set()
    paths = []

    while queue.queue:
        current_vertex = queue.dequeue()
        if current_vertex not in visited:
            print(current_vertex)
            queue.push(current_vertex)
            visited.add(current_vertex)
            for neighbor in graph.graph_dict.get(current_vertex, []):
                paths.append(neighbor)
                queue.push(neighbor)

    return paths
