"""
A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.
"""


# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
   
   
### BFS
from collections import deque
def get_cheapest_cost(rootNode):
  q = deque()
  q.appendleft((rootNode, rootNode.cost))
  
  min_cost = float("inf")
  
  while q:
    curr_node, cost = q.pop()
    
    # current node is leaf?
    if not curr_node.children:
      leaf_cost = curr_node.cost
      min_cost = min(min_cost, leaf_cost)
    
    _ = [q.appendleft(node, cost+node.cost) for node in curr_node.children]
    
  return min_cost
  
  
### DFS

def getCheapestCost(rootNode):
    n = rootNode.children

    if (n == 0):
        return rootNode.cost
    else:
        # initialize minCost to the largest integer in the system
        minCost = float("inf")
        for i in range(len(n)):
            tempCost = getCheapestCost(rootNode.child[i])
            if (tempCost < minCost):
                minCost = tempCost

    return minCost + rootNode.cost