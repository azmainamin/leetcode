import random

class RandomizedSet:
    """
    A hashmap {num : idx}
    A list to hold nums
    
    Remove:
    - Swap num to remove with last item
    - Update the idx of the swapped last item
    - Remove the last elem from list
    - Remove the elem from the map
    """
    def __init__(self):
        self.num_to_idx_map = {}
        self.nums = []
        self.current_idx = 0

    def insert(self, val: int) -> bool:
        if val in self.num_to_idx_map:
            return False
        else:
            self.num_to_idx_map[val] = self.current_idx
            self.nums.append(val)
            
            self.current_idx += 1
            return True
        

    def remove(self, val: int) -> bool:
        
        if val not in self.num_to_idx_map:
            return False
        else:
            curr_idx_of_val = self.num_to_idx_map[val]
            # swap with last elem in list
            last_elem = self.nums[-1]
            if len(self.nums) > 1:
                self.nums[curr_idx_of_val], self.nums[-1] = self.nums[-1], self.nums[curr_idx_of_val]
                # update idx in map
                self.num_to_idx_map[last_elem] = curr_idx_of_val
            
            # del last elem
            del self.nums[-1]
            del self.num_to_idx_map[val]

            
            self.current_idx -= 1
            
            return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()