from data_structure.stack.stack import Stack

def dfs(graph, start, visited=None):
    if visited is None:
        visited = Stack()

    if start not in visited.items:
        print(start)
        visited.push(start)

        for neighbor in graph.graph_dict.get(start, []):
            dfs(graph, neighbor, visited)