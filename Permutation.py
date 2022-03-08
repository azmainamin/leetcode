"""
BACKTRACKING SOLUTION

Permutations of a list of numbers
"""
class Solution:
    def permute(self, nums):
        res = []
        
        def dfs(first):
            if first == len(nums):
                return res.append(nums[:])
            
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first] 
                dfs(first+1)
                nums[first], nums[i] = nums[i], nums[first]
            
        dfs(0)
        return res
        
        
"""
BFS
"""
from collections import deque
from math import perm

class Solution:
    def permutation(self, nums):
        numsLength = len(nums)
        result = []
        permutations = deque()
        permutations.append([])

        for currentNumber in nums:
            # We will take all existing permutations and add the current number to create new permutations
            n = len(permutations)

            for _ in range(n):
                oldPermutation = permutations.popleft()
                # create new permuation by adding the number at every position
                for j in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currentNumber)
                    if len(newPermutation) == numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
        return result
