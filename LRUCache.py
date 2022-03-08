"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

"""
O(1) get means we have to use a hash map. O(1) put and the LRU cache eviction policy we need to remove a node at O(1) runtime.
So we have to use a doubly linked list.

We will be using a doubly linked list to create a dynamic list where most recent will be stored at head and least recent will be stored at the end.
So, when we get/put a node, we need to make sure its at the head (head.next) of our LL and when we need to remove a node i.e. evict, we will evict from tail. 

Get:
    - if node exists in hash map, return. otherwise return -1
    - once we get the node, we need to update to let us know that this is the most recently used node
    - we remove the node, and then add it back again at head.
Put:
    - if node exists, update the value. Remove and add back to head (most recent)
    - if node doesn't exist, and we are below capacity: add to head
    - if node doesn't exist, and we are over capacity:  remove the lru node (from tail), add new node to head. Update cache
"""

class Node:
    """
    Doubly LinkedList Node
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        # Head keeps track of most recently used and Tail keeps track of LRU
        self.head, self.tail = Node(0,0), Node(0,0)
        
        # Create the initial connections between the pseudo head and tail nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        - if node exists in hash map, return. otherwise return -1
        - once we get the node, we need to update to let us know that this is the most recently used node
        - we remove the node, and then add it back again at head.
        """
        if key in self.cache:
            node = self.cache[key]

            # most recently used node
            self.remove(node)
            self.add_to_head(node)
            
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        - if node exists, update the value. Remove and add back to head (most recent)
        - if node doesn't exist, and we are below capacity: add to head
        - if node doesn't exist, and we are over capacity:  remove the lru node (from tail), add new node to head. Update cache
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            self.remove(node)
            self.add_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.size += 1
            self.add_to_head(new_node)
            
            if self.size > self.capacity:
                lru_node = self.tail.prev
                self.remove(lru_node)
                del self.cache[lru_node.key]
                self.size -= 1
                
                
    def remove(self, node):
        """
        A -><- X -><- B ==> A -><- B
        """
        prev, new = node.prev, node.next
        
        prev.next = new
        new.prev = prev
                
    def add_to_head(self, node):
        """
        A-><-B ==> A -><- X -><- B
        """
        node.next = self.head.next
        node.prev = self.head
       
        # Order matters. Don't want to update self.head.next before updating self.head.next.prev
        self.head.next.prev = node
        self.head.next = node
       
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)