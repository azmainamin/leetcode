class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cache = [-1 for i in range(len(cost) + 1)]
        
        def climb(idx):
            if idx >= len(cost):
                return 0
            
            if cache[idx] != -1:
                return cache[idx]
            
            cache[idx] = min(cost[idx] + climb(idx + 1), cost[idx] + climb(idx + 2))
            
            return cache[idx]
        
        
        return min(climb(0), climb(1))