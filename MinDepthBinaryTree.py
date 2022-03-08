"""
MIN Depth of binary Tree
"""
import queue

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        IDEA: 
        - Use a BFS approach, keeping track of current depth
        - Moment we find a leaf node, we return current depth. This will ensure min depth
        """
        
        if root is None:
            return 0
        
        
        q = queue.Queue()
        
        initial_depth = 1
        root.value = initial_depth
        
        q.put(root)
        
        while not q.empty():
            node = q.get()
            current_depth = node.value
            
            # moment you see a leaf, return the current depth
            if node.left is None and node.right is None:
                return current_depth
            
            if node.left is not None:
                node.left.value = current_depth + 1
                q.put(node.left)
                
            if node.right is not None: 
                node.right.value = current_depth + 1
                q.put(node.right)
                
        return -1