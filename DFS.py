graph = {
    'A': ['B', 'C', 'D'],  # Node A is connected to nodes B, C, and D
    'B': ['E'],            # Node B is connected to node E
    'C': ['D', 'E'],       # Node C is connected to nodes D and E
    'D': [],               # Node D has no outgoing connections
    'E': []                # Node E has no outgoing connections
}


visited = set() # Create an empty set to keep track of visited nodes
def dfs(visited, graph, root):
    if root not in visited: # If the current node has not been visited yet
        print(root) # Print the current node
        visited.add(root) # Add the current node to the set of visited nodes
        for neighbour in graph[root]: # For each neighboring node of the current node
            dfs(visited, graph, neighbour) # Recursively call dfs for each neighboring node

dfs(visited, graph, 'A')
    
   
