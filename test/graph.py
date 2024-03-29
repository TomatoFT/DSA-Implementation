import sys

sys.path.append("./")


from algorithms.graph_search.BFS import BFS
from algorithms.graph_search.DFS import DFS
from data_structure.graph.graph import Node

if __name__ == "__main__":
    graph = Node([("Ha Noi", "Bac Ninh"), 
                  ("Bac Ninh", "Trung Quoc"), 
                  ("Ha Noi", "Da Nang"), 
                  ("Da Nang", "Ho Chi Minh"),
                  ("Ha Noi", "Ho Chi Minh"),
                  ("Bac Ninh", "Da Nang")])
    start_node = "Ha Noi"
    end_node = "Ho Chi Minh"
    all_paths = graph.get_all_paths(start_node, end_node)

    if not all_paths:
        print(f"No paths found from {start_node} to {end_node}.")
    else:
        print(f"All paths from {start_node} to {end_node}:")
        for path in all_paths:
            print(" -> ".join(path))

    DFS(graph)("Ha Noi")
    BFS(graph)("Ha Noi")