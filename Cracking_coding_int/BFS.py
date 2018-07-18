

#Finds shortest way from start node to end node
def BFSPath(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for neighboor in graph.get(node,[]):
            new_path =list(path)
            new_path.append(neighboor)
            queue.append(new_path)


#BigO V+E
#prints true if there is a way from i=one node to another and prints false if not
def BFS(graph, root,goal):
    visited = []
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighboors = graph[node]
            for neighboor in neighboors:
                queue.append(neighboor)
    for i in graph:
        if i not in visited:


    if goal in visited:
        return True
    else:
        return False
    # return visited

if __name__ == "__main__":
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    print(BFS(graph, 'A','G'))
