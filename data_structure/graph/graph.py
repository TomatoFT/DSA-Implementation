class Node:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            
            if end in self.graph_dict:
                self.graph_dict[end].append(start)
            else:
                self.graph_dict[end] = [start]

    def get_all_paths(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict or end not in self.graph_dict:
            return []

        paths = []
        for destination in self.graph_dict[start]:
            if destination not in path:
                print(f"Map for {destination} to {end} with {path}")
                new_paths = self.get_all_paths(destination, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
        
    def display_graph(self):
        print(self.graph_dict)
