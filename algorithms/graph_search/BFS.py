from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()

        if current_vertex not in visited:
            print(current_vertex)
            visited.add(current_vertex)

            for neighbor in graph.graph_dict.get(current_vertex, []):
                queue.append(neighbor)