def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start)
        visited.add(start)

        for neighbor in graph.graph_dict.get(start, []):
            dfs(graph, neighbor, visited)