"""
A. Build graph and inDegree map
  1. Graph -> Parent-Child, where we must process parent in order to process Child
  2. InDegree -> How many deps a node has

B. Add all nodes with 0 in degrees to a queue.
C. For each node with 0 deps, pop, then add to visited/sortedOrder. Then for each of their children, remove an inDegree. If the inDegree of that child is now 0, add to queue.
D. If len(sortedOrder) == total vertices, we have successfully traversed all nodes.
"""

from collections import deque

def topological_sort(vertices, edges):
  sorted_order = []
  if vertices <= 0: return sorted_order
  
  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)} # count of incoming edges
  graph = {i: [] for i in range(vertices)} #  adjacency list
  
  # b. Build graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)
    inDegree[child] += 1
  
  # c. Find all sources with 0 in degree
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)
  
  # d. For each source, add to sortedOrder, and subtract one from all of its children's in degrees
  # if a child's in degrees become zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sorted_order.append(vertex) # mark as visited
    for child in graph[vertex]:
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)
  
  if len(sorted_order) != vertices:
    return []
    
  return sorted_order