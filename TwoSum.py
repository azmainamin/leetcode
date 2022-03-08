class Solution:
    def twoSum(self, nums, target: int):
        """
        [3,2,4], target is 6
        
        for each find diff with target and store it in a dict
        as we iterate, see if the current number matches with the stored diff.
        in the above example, diff of 6-2 is 4, and when we are looking at item 
        at idx 2, we see that we have 4 in our stored diffs.
        
        6-3 = 3 -> {3:0} diff:idx
        6-2 = 4 -> {3:0, 4:1}
        6-4 = 2 -> in dict: fetch value of key 2, which is 1, return result [1,2]
        """
        diff_map = {}
        
        for idx in range(len(nums)):
            num = nums[idx]
            if num in diff_map:
                return [idx, diff_map[num]]
            else:
                diff = target - nums[idx]
                diff_map[diff] = idx