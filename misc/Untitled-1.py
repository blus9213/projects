

def child(a):
    print("child of " + str(a) + " are " + str(graph[a]))

def BFS(start_node):
    visited = set()
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)  # Process the node here (you can do other operations instead of printing)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph representation (dictionary) 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for BFS
start_node = 'A'

BFS(start_node)

child("B")





